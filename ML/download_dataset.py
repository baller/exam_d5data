from huggingface_hub import hf_hub_download

# 下载文件
file_path = hf_hub_download(
    repo_id="AdaptLLM/finance-tasks",
    filename="Headline/test.json",
    repo_type="dataset"
)

print(f"Downloaded file to: {file_path}")