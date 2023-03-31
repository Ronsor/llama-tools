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

## tokenizer_info.py

A simple script to print the training configuration for a tokenizer.

```
Usage: python tokenizer_info.py [model]
```

The configuration of the LLaMA tokenizer:

```
input: "/large_experiments/theorem/datasets/MERGED/all.test1.merged"
input_format: "text"
model_prefix: "spm_model_32k_200M_charcov099995_allowWSO__v2"
model_type: BPE
vocab_size: 32000
self_test_sample_size: 0
enable_differential_privacy: false
differential_privacy_noise_level: 0
differential_privacy_clipping_threshold: 0
character_coverage: 0.99995
input_sentence_size: 200000000
shuffle_input_sentence: true
seed_sentencepiece_size: 1000000
shrinking_factor: 0.75
max_sentence_length: 4192
num_threads: 80
num_sub_iterations: 2
max_sentencepiece_length: 16
split_by_unicode_script: true
split_by_number: true
split_by_whitespace: true
treat_whitespace_as_suffix: false
allow_whitespace_only_pieces: true
split_digits: true
required_chars: ""
byte_fallback: true
vocabulary_output_piece_score: true
hard_vocab_limit: true
use_all_vocab: false
unk_id: 0
bos_id: 1
eos_id: 2
pad_id: -1
unk_piece: "<unk>"
bos_piece: "<s>"
eos_piece: "</s>"
pad_piece: "<pad>"
unk_surface: " ⁇ "
train_extremely_large_corpus: false
```

## merge_tokenizer.py

A script to merge tokenizer model B into tokenizer model A. This may be useful
for finetuning.

```
Usage: python merge_tokenizer.py [output model] [model a] [model b]
```

## License

Copyright &copy; 2023 Ronsor Labs. All rights reserved.

This software is provided under the MIT license. For more information, see
the `LICENSE` in this repository. Third-party components, especially those
in `sputil/` may be provided under a different license.
