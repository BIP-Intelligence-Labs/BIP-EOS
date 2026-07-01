from bip_eos.runtime.runtime import create_runtime

def main() -> None:
    runtime = create_runtime()
    runtime.start()

if __name__ == "__main__":
    main()
