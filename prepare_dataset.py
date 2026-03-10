import os
import random
import shutil
from pathlib import Path


# dataset split ratio
TRAIN_RATIO = 0.9
VAL_RATIO = 0.09
TEST_RATIO = 0.01

random.seed(42)


BASE_DIR = Path(__file__).parent

RAW_IMG = BASE_DIR / "dataset_raw/images"
RAW_LBL = BASE_DIR / "dataset_raw/labels"

DATA_IMG = BASE_DIR / "dataset/images"
DATA_LBL = BASE_DIR / "dataset/labels"

TRAIN_IMG = DATA_IMG / "train"
VAL_IMG = DATA_IMG / "val"
TEST_IMG = DATA_IMG / "test"

TRAIN_LBL = DATA_LBL / "train"
VAL_LBL = DATA_LBL / "val"
TEST_LBL = DATA_LBL / "test"


def main():

    # create folders
    TRAIN_IMG.mkdir(parents=True, exist_ok=True)
    VAL_IMG.mkdir(parents=True, exist_ok=True)
    TEST_IMG.mkdir(parents=True, exist_ok=True)

    TRAIN_LBL.mkdir(parents=True, exist_ok=True)
    VAL_LBL.mkdir(parents=True, exist_ok=True)
    TEST_LBL.mkdir(parents=True, exist_ok=True)

    images = [f for f in os.listdir(RAW_IMG) if f.endswith(".jpg")]

    random.shuffle(images)

    total = len(images)

    train_split = int(total * TRAIN_RATIO)
    val_split = int(total * (TRAIN_RATIO + VAL_RATIO))

    train = images[:train_split]
    val = images[train_split:val_split]
    test = images[val_split:]

    print("Total images:", total)
    print("Train:", len(train))
    print("Val:", len(val))
    print("Test:", len(test))

    # copy train
    for img in train:

        shutil.copy(RAW_IMG / img, TRAIN_IMG / img)

        label = img.replace(".jpg", ".txt")

        shutil.copy(RAW_LBL / label, TRAIN_LBL / label)

    # copy val
    for img in val:

        shutil.copy(RAW_IMG / img, VAL_IMG / img)

        label = img.replace(".jpg", ".txt")

        shutil.copy(RAW_LBL / label, VAL_LBL / label)

    # copy test
    for img in test:

        shutil.copy(RAW_IMG / img, TEST_IMG / img)

        label = img.replace(".jpg", ".txt")

        shutil.copy(RAW_LBL / label, TEST_LBL / label)

    print("Dataset split finished.")


if __name__ == "__main__":
    main()