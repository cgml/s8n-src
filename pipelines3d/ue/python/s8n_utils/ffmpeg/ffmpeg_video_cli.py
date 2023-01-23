import argparse
import os
import datetime as dt
import shutil

FFMPEG_COMMAND = "C:/s8n/system/tools/ffmpeg/bin/ffmpeg.exe"
S8N_GENERATED_UE_ROOT = "C:/s8n-generated/ue"


def execute(project_path: str, resoltion: str, format: str):
    input_dir = f"{S8N_GENERATED_UE_ROOT}/{project_path}"
    work_dir = f"{S8N_GENERATED_UE_ROOT}/work_dir"
    if os.path.exists(work_dir):
        shutil.rmtree(work_dir)
    os.makedirs(work_dir, exist_ok=True)
    counter = 1
    for f in os.listdir(input_dir):
        print(f)
        if format in f:
            shutil.copy(f"{input_dir}/{f}", f"{work_dir}/{counter:04d}.{format}")
            counter += 1

    project_code = project_path.replace('/', '-').replace('\\', '-')
    output_dir = f"{S8N_GENERATED_UE_ROOT}/final_mp4"
    os.makedirs(output_dir, exist_ok=True)
    output_file = f"{dt.datetime.now().strftime('%Y-%m-%d-%H-%M')}-{project_code}.mp4"
    output_path = f"{output_dir}/{output_file}"
    pwd = os.curdir
    os.chdir(input_dir)
    print(input_dir)
    if format == 'png':
        command = f"{FFMPEG_COMMAND} -r 24 -f image2 -s {resoltion} -i " \
                  f"{work_dir}/%04d.{format} -pix_fmt yuv420p -vcodec libx264 -crf 10 {output_path}".replace('/', '\\')

    else:
        command = f"{FFMPEG_COMMAND} -r 24 -f image2 -s {resoltion} -i " \
                  f"{work_dir}/%04d.{format} -vcodec libx264 -crf 10 {output_path}".replace('/', '\\')
    print(command)
    os.system(command)
    os.chdir(pwd)
    print(f'Ready at: {output_dir}')

def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("project", help="Relative project path from c:/s8n-generated/ue. E.g. experimental/2023-01-01-mustang-01")
    parser.add_argument("--resolution", default="1920x1080", help="Resolution. E.g. 3840x2160")
    parser.add_argument("--format", default="jpeg", help="Format, e.g. jpeg")
    parser.add_argument("--fps", default="24", help="FPS e.g 30")
    args = parser.parse_args()
    execute(project_path=args.project, resoltion=args.resolution, format=args.format)

if __name__ == "__main__":
    cli()
