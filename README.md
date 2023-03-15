# LLaMA Tools

Random tools for playing with the LLaMA LLM and its tokenizer.

## add_tokens.py

A simple script to add tokens from a text file to the tokenizer. You'll
probably still have to finetune the model so it knows about these new tokens.
Requires `protobuf` installed, but not `sentencepiece` (though you'll probably
still want that).

```
Usage: python add_tokens.py [original model] [output model] [token list]
```

* `[original model]` is the path to the original tokenizer model, which is
included as `etc/tokenizer.model` for convenience.
* `[output model]` is the file path for the modified tokenizer model, and
should not be the same as `[original model]`
* `[token list]` is the name of a text file with the following format:

```
N normal token
C <control token>
U user defined token
UB YW5vdGhlciB1c2VyIHRva2Vu
```

Lines begin with the token type, then are followed by a space and then the
token value (until a newline) OR are followed by `B` and then a space to
indicate the token value is base64 encoded. See `test_list.txt`.

For information on token types, see `sputil/sentencepiece_model.proto`
and <https://github.com/google/sentencepiece>.

## License

Copyright &copy; 2023 Ronsor Labs. All rights reserved.

This software is provided under the MIT license. For more information, see
the `LICENSE` in this repository. Third-party components, especially those
in `sputil/` may be provided under a different license.
