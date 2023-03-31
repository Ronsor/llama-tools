#!/usr/bin/env python
import sys, base64
import sputil.sentencepiece_model_pb2 as model

if len(sys.argv) != 4:
	print("Usage: python merge_tokenizer.py [output model] [model a] [model b]")
	sys.exit(1)

m1 = model.ModelProto()
m1.ParseFromString(open(sys.argv[2], "rb").read())

m2 = model.ModelProto()
m2.ParseFromString(open(sys.argv[3], "rb").read())

existing = set([
  (x.piece, x.type) for x in m1.pieces
])

for y in m2.pieces:
  if (y.piece, y.type) in existing: continue
  m1.pieces.append(y)
  m1.trainer_spec.vocab_size += 1

open(sys.argv[1], 'wb').write(m1.SerializeToString())
