# ffmpeg -r 20 -f image2 -i slideshow/%d.png -y -s 320x240 -aspect 4:3 out.mp4

cd C:\rendered\DMX
C:\s8n\system\tools\ffmpeg\bin\ffmpeg.exe -r 20 -f image2 -i "DMXPrevis_Animations.%%04d.png" -vcodec libx264 -crf 18  -y -s 320x240 C:\rendered\DMXPrevis_Animations_png.mp4
cd C:\s8n\system\src\pipelines\s8n-alpha\src\scripts
