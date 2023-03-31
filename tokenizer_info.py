#!/usr/bin/env python
import sys, base64
import sputil.sentencepiece_model_pb2 as model

if len(sys.argv) != 2:
	print("Usage: python tokenizer_info.py [model]")
	sys.exit(1)

m = model.ModelProto()
m.ParseFromString(open(sys.argv[1], "rb").read())

print(m.trainer_spec)
