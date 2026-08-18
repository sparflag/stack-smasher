# Stack Smasher (`stack-smasher`)

**Category:** binary exploitation · **Difficulty:** medium · **Points:** 300

A 64-bit ELF reads your input into a fixed stack buffer with no bounds check. Overflow the saved return address to redirect execution to the hidden win() function, which prints the seed that decrypts your flag.

## Run it

```bash
docker build -t sparflag/stack-smasher .
# `deca-ai start stack-smasher` (or the web UI) prints the docker run line with your
# SPARFLAG_SERVER + SPARFLAG_INSTANCE_TOKEN
```

## Recover the flag

The delivery blob is Fernet ciphertext. Discover the key seed, derive the Fernet key, then decrypt.

The plaintext flag is never written to disk or served — only the encoded delivery blob
is. When you have it:

```bash
deca-ai submit stack-smasher 'sparflag{...}'
```

## Hints

- How many bytes until you reach the saved return address?
- objdump -d the binary and find the address of win().
- Pad to the return address, then overwrite it with win()'s address.
