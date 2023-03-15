#!/usr/bin/env python
import sys, base64
import sputil.sentencepiece_model_pb2 as model

if len(sys.argv) != 4:
	print("Usage: python add_tokens.py [original model] [output model] [token list]")
	sys.exit(1)

m = model.ModelProto()
m.ParseFromString(open(sys.argv[1], "rb").read())

lines_clean = filter(None, [x.strip() for x in open(sys.argv[3], "r").read().split('\n')])
for line in lines_clean:
	print('ADD:', line)
	type = line[0]
	if type != 'C' and type != 'U' and type != 'N':
		print("Invalid token type")
		sys.exit(1)
	if line[1] == 'B':
		token = base64.b64decode(line[3:])
	else:
		token = line[2:].encode('utf-8')
	new_token = model.ModelProto().SentencePiece()
	new_token.piece = token
	new_token.score = 0
	new_token.type = 3 if type == 'C' else 4 if type == 'U' else 1
	m.pieces.append(new_token)

open(sys.argv[2], 'wb').write(m.SerializeToString())
