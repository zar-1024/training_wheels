def download_from_url(url):
    run(f'yt-dlp.exe {url}', shell=True)
