class Config:
    canPhones ="./wordsyn/jyutping-wong-44100-v9/jyutping-wong/"
    mandPhones ="./wordsyn/pinyin-yali-44100/"
    text= "1/01/1991，32。翻译都要执行多个翻译系统，这带来巨大的计算成本。如今，许多领域都正在被神经网路技术颠覆。测试4"
    phrase = [text,]  # 以后可以放多个
    language= "c"
    # play=
    crossfade=True
    # outfile="./outfile_test/output_cantonese_test.wav"
    out_folder="./outfile_test/"
    volume = 80
    # speed

args = Config