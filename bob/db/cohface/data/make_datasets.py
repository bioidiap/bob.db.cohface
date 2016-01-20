#!/usr/bin/env python
# encoding: utf-8
# Guillaume HEUSCH <guillaume.heusch@idiap.ch>
# Wed 20 Jan 09:05:20 CET 2016

import random
import os
import re
import sys

random.seed(5)

# train -> 12 subjects
# dev -> 12 subjects
# test -> 16 subjects

subjects = range(1, 41)

# =======================
# === training set(s) === 
# =======================
train = random.sample(subjects, 12)

# === all conditions ===
sessions = [0, 2]
train_examples = []
for subj in train:
  for s in sessions:
    f = str(subj) + "/" + str(s) + "/" + "data"
    train_examples.append(f)

train_list_file = open("train_all.txt", "w")
for f in train_examples:
  train_list_file.write("{0}\n".format(f))
train_list_file.close()

# === clean condition only ===
sessions = [0]
train_examples = []
for subj in train:
  for s in sessions:
    f = str(subj) + "/" + str(s) + "/" + "data"
    train_examples.append(f)

train_list_file = open("train_clean.txt", "w")
for f in train_examples:
  train_list_file.write("{0}\n".format(f))

# remove training subjects from the pool of subjects
for t in train:
  subjects.remove(t)

# =======================
# === development set ===
# =======================
dev = random.sample(subjects, 12)

# === all conditions ===
sessions = [0, 2]
dev_examples = []
for subj in dev:
  for s in sessions:
    f = str(subj) + "/" + str(s) + "/" + "data"
    dev_examples.append(f)

dev_list_file = open("dev_all.txt", "w")
for f in dev_examples:
  dev_list_file.write("{0}\n".format(f))
dev_list_file.close()

# === clean condition only ===
sessions = [0]
dev_examples = []
for subj in dev:
  for s in sessions:
    f = str(subj) + "/" + str(s) + "/" + "data"
    dev_examples.append(f)

dev_list_file = open("dev_clean.txt", "w")
for f in dev_examples:
  dev_list_file.write("{0}\n".format(f))

# remove dev subjects from the pool of subjects
for d in dev:
  subjects.remove(d)

# ===============================
# === train + development set ===
# ===============================
train_dev = train + dev

# === all conditions ===
sessions = [0, 2]
train_dev_examples = []
for subj in train_dev:
  for s in sessions:
    f = str(subj) + "/" + str(s) + "/" + "data"
    train_dev_examples.append(f)

train_dev_list_file = open("traindev_all.txt", "w")
for f in train_dev_examples:
  train_dev_list_file.write("{0}\n".format(f))
train_dev_list_file.close()

# === clean condition only ===
sessions = [0]
train_dev_examples = []
for subj in train_dev:
  for s in sessions:
    f = str(subj) + "/" + str(s) + "/" + "data"
    train_dev_examples.append(f)

train_dev_list_file = open("traindev_clean.txt", "w")
for f in train_dev_examples:
  train_dev_list_file.write("{0}\n".format(f))

# ================
# === test set ===
# ================
test = subjects

# === all conditions ===
sessions = [0, 2]
test_examples = []
for subj in test:
  for s in sessions:
    f = str(subj) + "/" + str(s) + "/" + "data"
    test_examples.append(f)

test_list_file = open("test_all.txt", "w")
for f in test_examples:
  test_list_file.write("{0}\n".format(f))
test_list_file.close()

# === clean condition only ===
sessions = [0]
test_examples = []
for subj in test:
  for s in sessions:
    f = str(subj) + "/" + str(s) + "/" + "data"
    test_examples.append(f)

test_list_file = open("test_clean.txt", "w")
for f in test_examples:
  test_list_file.write("{0}\n".format(f))

