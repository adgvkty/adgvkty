from pytube import YouTube


def get_video(link):
    yt = YouTube(link)
    stream = yt.streams.filter(adaptive=True)
    return stream[0]


def download(video):
    try:
        dc = input('Choose directory: \n '
                   '1. Script directory \n'
                   ' 2. Input Own \n ')
        if dc == '2':
            dc = input('Ok, your own directory: ')
            video.download(dc)
        else:
            video.download()

        print('downloading...')
    except Exception as e:
        print(e)


def main():
    link = input('Video Link: ')
    video = get_video(link)
    download(video)
    print('Done!')


main()
