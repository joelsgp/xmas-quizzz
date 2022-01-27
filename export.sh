#!/usr/bin/env bash
git archive -o quizzz.tar.gz HEAD
git archive -o quizzz.zip HEAD
git bundle create quizzz.bundle main
# bypass email attachment limitations
quizzz_files='quizzz.bundle quizzz.tar.gz quizzz.zip'
for quizzz in $quizzz_files
do
    gpg -a --batch --yes --symmetric --passphrase "BOB" $quizzz
done
