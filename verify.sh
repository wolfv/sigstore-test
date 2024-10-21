# which sigstore

sigstore verify github  \
    --bundle wolfv-sigstore-test-attestation-2102070.sigstore.json \
    --cert-identity https://github.com/wolfv/sigstore-test/.github/workflows/action.yaml@refs/heads/main \
    sha256:db468f8ac06acd10fef9c6bde46ce99abf75aa8578fe2b0948b3c08dbb798fba