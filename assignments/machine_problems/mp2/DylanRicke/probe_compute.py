"""probe_compute.py - CIS 531/731 MP2 Part 2: probe for CUDA and route to GPU or CPU."""
import torch


def select_device():
    """Return the compute device to use, printing which pool is active."""
    if torch.cuda.is_available():
        count = torch.cuda.device_count()
        name = torch.cuda.get_device_name(0)
        print(f"CUDA available: {count} device(s), device 0 = {name}")
        print("GPU Pool Active - Batch Embedding/Whisper Ready")
        return torch.device("cuda")
    print("CUDA not available on this system.")
    print("CPU-Only Fallback Active")
    return torch.device("cpu")


def faiss_backend():
    """Report whether FAISS can use the GPU or must use its CPU index."""
    import faiss
    gpus = faiss.get_num_gpus() if hasattr(faiss, "get_num_gpus") else 0
    if gpus > 0:
        print(f"FAISS: GPU index available ({gpus} GPU(s))")
        return "gpu"
    print("FAISS: using CPU index (faiss-cpu)")
    return "cpu"


if __name__ == "__main__":
    print(f"PyTorch version: {torch.__version__}")
    device = select_device()
    backend = faiss_backend()

    # Smoke test: run a small tensor operation on the selected device
    x = torch.randn(1000, 1000, device=device)
    y = x @ x.T
    print(f"Smoke test OK on {device}: result shape {tuple(y.shape)}")