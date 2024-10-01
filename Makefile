FFMPEG = ffmpeg
RECEIVER_IP = localhost
PORT = 5000
# Replace WEBCAM with the actual webcam name
WEBCAM = "WEBCAM"
PRESET = ultrafast
CODEC = libx264
FORMAT = mpegts

# Target for getting the list of webcams
get-webcam:
	$(FFMPEG) -list_devices true -f dshow -i dummy

# Target for the sender (replace RECEIVER_IP with the actual IP)
sender:
	$(FFMPEG) -f dshow -i video=$(WEBCAM) -vcodec $(CODEC) -preset $(PRESET) -tune zerolatency -f $(FORMAT) tcp://$(RECEIVER_IP):$(PORT)

# Target for the receiver
receiver:
	ffplay -fflags nobuffer -fflags discardcorrupt -flags low_delay -vf setpts=0  tcp://0.0.0.0:$(PORT)/?listen