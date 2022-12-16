from .crawler import crawl


def main() -> None:
    """ main function """
    print("main")
    res = crawl(1)
    print(res)


if __name__ == "__main__":
    main()
