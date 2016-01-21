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

# sessions 0 and 1 -> spot
# sessions 2 and 3 -> natural light


subjects = range(1, 41)

# =======================
# === training set(s) === 
# =======================
train = random.sample(subjects, 12)

# === all conditions ===
sessions = [0, 1, 2, 3]
train_examples = []
for subj in train:
  for s in sessions:
    f = str(subj) + "/" + str(s) + "/" + "data"
    train_examples.append(f)

train_list_file = open("all/train.txt", "w")
for f in train_examples:
  train_list_file.write("{0}\n".format(f))
train_list_file.close()

# === clean condition only ===
sessions = [0, 1]
train_examples = []
for subj in train:
  for s in sessions:
    f = str(subj) + "/" + str(s) + "/" + "data"
    train_examples.append(f)

train_list_file = open("clean/train.txt", "w")
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
sessions = [0, 1, 2, 3]
dev_examples = []
for subj in dev:
  for s in sessions:
    f = str(subj) + "/" + str(s) + "/" + "data"
    dev_examples.append(f)

dev_list_file = open("all/dev.txt", "w")
for f in dev_examples:
  dev_list_file.write("{0}\n".format(f))
dev_list_file.close()

# === clean condition only ===
sessions = [0, 1]
dev_examples = []
for subj in dev:
  for s in sessions:
    f = str(subj) + "/" + str(s) + "/" + "data"
    dev_examples.append(f)

dev_list_file = open("clean/dev.txt", "w")
for f in dev_examples:
  dev_list_file.write("{0}\n".format(f))

# remove dev subjects from the pool of subjects
for d in dev:
  subjects.remove(d)

# ================
# === test set ===
# ================
test = subjects

# === all conditions ===
sessions = [0, 1, 2, 3]
test_examples = []
for subj in test:
  for s in sessions:
    f = str(subj) + "/" + str(s) + "/" + "data"
    test_examples.append(f)

test_list_file = open("all/test.txt", "w")
for f in test_examples:
  test_list_file.write("{0}\n".format(f))
test_list_file.close()

# === clean condition only ===
sessions = [0, 1]
test_examples = []
for subj in test:
  for s in sessions:
    f = str(subj) + "/" + str(s) + "/" + "data"
    test_examples.append(f)

test_list_file = open("clean/test.txt", "w")
for f in test_examples:
  test_list_file.write("{0}\n".format(f))

