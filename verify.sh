# which sigstore

sigstore verify github  \
    --bundle wolfv-sigstore-test-attestation-2627564.sigstore.json \
    --cert-identity https://github.com/wolfv/sigstore-test/.github/workflows/action.yaml@refs/heads/main \
    sha256:96f5b18fb6fa4545bd78c6a5f58217b73bd16b45bf06b293ad50a95c510a1f38