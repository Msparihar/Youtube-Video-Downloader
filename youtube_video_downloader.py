import pafy

url = "https://www.youtube.com/watch?v=u1kXyjpOOvc"

video = pafy.new(url)

best = video.getbest()

best.download(quiet=False)