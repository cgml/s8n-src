import argparse
import os
import datetime as dt
import shutil

FFMPEG_COMMAND = "C:/s8n/system/tools/ffmpeg/bin/ffmpeg.exe"
S8N_GENERATED_UE_ROOT = "C:/s8n-generated/ue"


def execute(audio_path: str):

    output_path = f"{audio_path}.mp3"
    # pwd = os.curdir
    # os.chdir(input_dir)
    # print(input_dir)
    command = f"{FFMPEG_COMMAND} -i {audio_path} -q:a 0 -map a {output_path}".replace('/', '\\')
    print(command)
    os.system(command)
    # os.chdir(pwd)
    # print(f'Ready at: {output_dir}')

def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("audio", help="Path to audio file")
    args = parser.parse_args()
    execute(audio_path=args.audio)


if __name__ == "__main__":
    cli()


