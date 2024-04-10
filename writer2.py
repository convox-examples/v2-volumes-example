import time

def main():
    while True:
        with open("/my/shared/data/writer2.txt", "a") as f:
            f.write(f"Writer 2 wrote at {time.ctime()}\n")
        time.sleep(12)  # Write every 12 seconds

if __name__ == "__main__":
    main()
