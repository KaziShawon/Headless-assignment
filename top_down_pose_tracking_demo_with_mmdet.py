# Copyright (c) OpenMMLab. All rights reserved.
import concurrent.futures
import os
import warnings
from argparse import ArgumentParser
from video_get import VideoGet

import cv2
import glob
import numpy as np

from mmpose.apis import (get_track_id, inference_top_down_pose_model,
                         init_pose_model, process_mmdet_results,
                         vis_pose_tracking_result)
from mmpose.datasets import DatasetInfo

try:
    from mmdet.apis import inference_detector, init_detector
    has_mmdet = True
except (ImportError, ModuleNotFoundError):
    has_mmdet = False


def main():
    """Visualize the demo images.

    Using mmdet to detect the human.
    """
    parser = ArgumentParser()
    parser.add_argument('det_config', help='Config file for detection')
    parser.add_argument('det_checkpoint', help='Checkpoint file for detection')
    parser.add_argument('pose_config', help='Config file for pose')
    parser.add_argument('pose_checkpoint', help='Checkpoint file for pose')
    parser.add_argument('--path', type=str, help='Video path')
    parser.add_argument(
        '--show',
        action='store_true',
        default=False,
        help='whether to show visualizations.')
    parser.add_argument(
        '--out-video-root',
        default='',
        help='Root of the output video file. '
        'Default not saving the visualization video.')
    parser.add_argument(
        '--device', default='cuda:0', help='Device used for inference')
    parser.add_argument(
        '--det-cat-id',
        type=int,
        default=1,
        help='Category id for bounding box detection model')
    parser.add_argument(
        '--bbox-thr',
        type=float,
        default=0.3,
        help='Bounding box score threshold')
    parser.add_argument(
        '--kpt-thr', type=float, default=0.3, help='Keypoint score threshold')
    parser.add_argument(
        '--use-oks-tracking', action='store_true', help='Using OKS tracking')
    parser.add_argument(
        '--tracking-thr', type=float, default=0.3, help='Tracking threshold')
    parser.add_argument(
        '--euro',
        action='store_true',
        help='Using One_Euro_Filter for smoothing')
    parser.add_argument(
        '--radius',
        type=int,
        default=4,
        help='Keypoint radius for visualization')
    parser.add_argument(
        '--thickness',
        type=int,
        default=1,
        help='Link thickness for visualization')

    assert has_mmdet, 'Please install mmdet to run the demo.'

    args = parser.parse_args()

    assert args.show or (args.out_video_root != '')
    assert args.det_config is not None
    assert args.det_checkpoint is not None

    det_model = init_detector(
        args.det_config, args.det_checkpoint, device=args.device.lower())
    # build the pose model from a config file and a checkpoint file
    pose_model = init_pose_model(
        args.pose_config, args.pose_checkpoint, device=args.device.lower())

    dataset = pose_model.cfg.data['test']['type']
    dataset_info = pose_model.cfg.data['test'].get('dataset_info', None)
    if dataset_info is None:
        warnings.warn(
            'Please set `dataset_info` in the config.'
            'Check https://github.com/open-mmlab/mmpose/pull/663 for details.',
            DeprecationWarning)
    else:
        dataset_info = DatasetInfo(dataset_info)

    # Getting All the four videos from the video path
    video_path = args.path
    video_list = glob.glob(video_path + '/*.mp4')

    assert len(video_list)==4, f'There should be mostly four videos in the path'

    # Initializing Video capture and asserting if it fails to load

    for k, video in enumerate(video_list):
        if k == 0:
            cap1 = cv2.VideoCapture(video)
            assert cap1.isOpened(), f'Faild to load video file {video_list[0]}'
        elif k == 1:
            cap2 = cv2.VideoCapture(video)
            assert cap2.isOpened(), f'Faild to load video file {video_list[1]}'
        elif k == 2:
            cap3 = cv2.VideoCapture(video)
            assert cap3.isOpened(), f'Faild to load video file {video_list[2]}'
        elif k == 3:
            cap4 = cv2.VideoCapture(video)
            assert cap4.isOpened(), f'Faild to load video file {video_list[3]}'
            

    fps = None

    if args.out_video_root == '':
        save_out_video = False
    else:
        os.makedirs(args.out_video_root, exist_ok=True)
        save_out_video = True

    # Getting the minimum fps and highest size from all the videos.
    # Initializint videoWriter method, it will output .mp4 file.

    if save_out_video:
        fps = min(cap1.get(cv2.CAP_PROP_FPS),
                    cap2.get(cv2.CAP_PROP_FPS),
                    cap3.get(cv2.CAP_PROP_FPS),
                    cap4.get(cv2.CAP_PROP_FPS))
        size = (int(max(cap1.get(cv2.CAP_PROP_FRAME_WIDTH),
                        cap2.get(cv2.CAP_PROP_FRAME_WIDTH),
                        cap3.get(cv2.CAP_PROP_FRAME_WIDTH),
                        cap4.get(cv2.CAP_PROP_FRAME_WIDTH))),
                int(max(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT),
                        cap2.get(cv2.CAP_PROP_FRAME_HEIGHT),
                        cap3.get(cv2.CAP_PROP_FRAME_HEIGHT),
                        cap4.get(cv2.CAP_PROP_FRAME_HEIGHT))))
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        videoWriter = cv2.VideoWriter('output.mp4', fourcc,fps, size)

    # optional
    return_heatmap = False

    # e.g. use ('backbone', ) to return backbone feature
    output_layer_names = None

    def threadVideoGet(source=None):
        """
        Dedicated thread for grabbing video frames with VideoGet object.
        :param: source will take video path and pass it to VideoGet
        """

        video_getter = VideoGet(source).start()
        while True:
            if (cv2.waitKey(1) == ord("q")) or video_getter.stopped:
                video_getter.stop()
                break

            frame = video_getter.frame
            success = video_getter.grabbed
        return frame, success


    def sort_video_list(video_list=None):
        """
        Param: video_list: It takes list of paths of the four videos

        The purpose of this function is to take video_list and put the
        lengthiest video at first position in the list.
        """

        prev_video_length = 0
        for index, v in  enumerate(video_list):
            cap = cv2.VideoCapture(v)
            frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
            fps = int(cap.get(cv2.CAP_PROP_FPS))

            # calculate dusration of the video
            video_length = int(frames / fps)

            if prev_video_length < video_length:
                video_list[index], video_list[0] = video_list[0], video_list[index]
            prev_video_length = video_length
            
        return video_list

    sorted_video_list = sort_video_list(video_list=video_list)


    next_id = 0
    pose_results = []

    while True:

        pose_results_last = pose_results

        # Getting image and success from each thread.
        img1, flag1 = threadVideoGet(source=sorted_video_list[0])
        img2, flag2 = threadVideoGet(source=sorted_video_list[1])
        img3, flag3 = threadVideoGet(source=sorted_video_list[2])
        img4, flag4 = threadVideoGet(source=sorted_video_list[3])

        # If the lengthiest one returns no frame then exit the loop
        if flag1 != True:
            break

        # for the shorter length videos keep generating blank images.
        elif flag2 != True:
            img2 = np.zeros((size[0], size[1], 3), dtype=np.uint8)
        elif flag3 != True:
            img3 = np.zeros((size[0], size[1], 3), dtype=np.uint8)
        elif flag4 != True:
            img4 = np.zeros((size[0], size[1], 3), dtype=np.uint8)

        # Using OpenCV (vconcat, hconcat)
        Vertical1 = np.concatenate((img1, img2), axis=0)
        Vertical2 = np.concatenate((img3, img4), axis=0)
        final = cv2.hconcat([Vertical1, Vertical2])
        final_image = cv2.resize(final, size, interpolation = cv2.INTER_LINEAR)

        # test a single image, the resulting box is (x1, y1, x2, y2)
        mmdet_results = inference_detector(det_model, final_image)

        # keep the person class bounding boxes.
        person_results = process_mmdet_results(mmdet_results, args.det_cat_id)

        # test a single image, with a list of bboxes.
        pose_results, returned_outputs = inference_top_down_pose_model(
            pose_model,
            final_image,
            person_results,
            bbox_thr=args.bbox_thr,
            format='xyxy',
            dataset=dataset,
            dataset_info=dataset_info,
            return_heatmap=return_heatmap,
            outputs=output_layer_names)

        # get track id for each person instance
        pose_results, next_id = get_track_id(
            pose_results,
            pose_results_last,
            next_id,
            use_oks=args.use_oks_tracking,
            tracking_thr=args.tracking_thr,
            use_one_euro=args.euro,
            fps=fps)

        # show the results
        vis_img = vis_pose_tracking_result(
            pose_model,
            final_image,
            pose_results,
            radius=args.radius,
            thickness=args.thickness,
            dataset=dataset,
            dataset_info=dataset_info,
            kpt_score_thr=args.kpt_thr,
            show=False)

        if args.show:
            cv2.imshow('Image', vis_img)

        if save_out_video:
            videoWriter.write(vis_img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap1.release() and cap2.release() and cap3.release() and cap4.release()
    if save_out_video:
        videoWriter.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
