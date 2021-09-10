echo "Cloning Repo...."
git clone https://github.com/akhilbaiju/VideoPlayerBot /VideoPlayerBot
cd /VideoPlayerBot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 main.py