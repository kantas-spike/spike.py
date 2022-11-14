#!/usr/bin/env python3
import argparse
import glob
import os
import sys

# 前提として、スパイクフォルダは"~/spike"、プレフィックスの区切り文字は"_"とする
SPIKE_DIR = os.path.expanduser("~/spike")
PREFIX_SEPARATOR = "_"

parser = argparse.ArgumentParser(description='引数で指定されたタスク名の作業フォルダをVsCodeで開く')
parser.add_argument('task_name', metavar='TASK_NAME', type=str, nargs=1, help='タスク名')

if len(sys.argv) < 2:
    print("引数に作業名を指定してください\n")
    parser.print_help()
    sys.exit(1)

# 引数で指定された作業名を取得する
args = parser.parse_args()
task_name = args.task_name[0]

# スパイクフォルダの存在チェック
if not os.path.isdir(SPIKE_DIR):
    print(f"creating {SPIKE_DIR} ...")
    os.makedirs(SPIKE_DIR)

target_dir = None
max_no = 0
# スパイクフォルダからディレクトリ一覧を取得
for d in glob.glob(os.path.join(SPIKE_DIR, "*/")):
    d_name = os.path.basename(os.path.dirname(d))
    no_and_name = d_name.split(PREFIX_SEPARATOR, 1)

    if len(no_and_name) != 2:
        print(f"ignore bad format: {d_name}...")
        continue

    if no_and_name[1] == task_name:
        # 既存のタスクのため、d を開く
        print(f"{no_and_name[1]} already exists: {d}")
        target_dir = d
        break

    try:
        no = int(no_and_name[0])
    except ValueError:
        print(f"ignore bad format: {d_name}...")
        continue

    if no > max_no:
        max_no = no

if target_dir is None:
    next_no = max_no + 1
    target_dir = os.path.join(SPIKE_DIR, f"{next_no:02}_{task_name}")
    print(f"creating {target_dir}...")
    os.makedirs(target_dir)

print(f"code '{target_dir}' ...")
os.system(f"code '{target_dir}'")
sys.exit(0)
