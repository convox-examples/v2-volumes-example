import time

def main():
    while True:
        with open("/my/shared/data/writer1.txt", "a") as f:
            f.write(f"Writer 1 wrote at {time.ctime()}\n")
        time.sleep(10)  # Write every 10 seconds

if __name__ == "__main__":
    main()
