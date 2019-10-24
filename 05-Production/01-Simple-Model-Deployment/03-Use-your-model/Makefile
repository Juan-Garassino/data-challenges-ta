

eval_local:
	-@python -m predict

eval_gcp_online:
	-@gcloud ai-platform predict --model ${MODEL_NAME} \
        --json-instances ../data/test_sample.json \
        --version baseline