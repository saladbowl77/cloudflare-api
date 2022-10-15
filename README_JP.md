[English](/README.md) / 日本語

## cl_apiについて
このライブラリーはCLoudflare APIの操作を簡単にするものです。  
Cloudflare APIのパラメーターに準拠しています。  
そのためAPIの [ドキュメント](https://api.cloudflare.com/#dns-records-for-a-zone-properties)もお読みください

### how to install
pipを使ってインストールできます

```shell
pip3 install git+https://github.com/saladbowl77/cloudflare-api
```

または

```shell
python3 -m pip install --user git+https://github.com/saladbowl77/cloudflare-api
```

## sampleについて
### cl_ddns.py
このファイルはCloudflare APIを用いてDDNSをします。
このコードを実行するにはCloudflareのアカウントとAPIKeyが必要です。