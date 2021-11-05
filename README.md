# ApexTrackerPy
Python library that calls the ApexLegends tracker API

ApexLegendsトラッカーAPIを呼び出すpythonライブラリ

# Install
It will be installed by `pip3 install ApexTrackerPy`.

You can also use git to install

`pip3 install git+https://github.com/nerrog/ApexTrackerPy.git`


`pip3 install ApexTrackerPy`でインストールされます

gitを使用してインストールすることもできます

`pip3 install git+https://github.com/nerrog/ApexTrackerPy.git`

# usage

All return values are in json.
In the future, we plan to implement return methods other than json.

返り値はすべてjsonです。
将来的にはjson以外の返却方法も実装する予定です

## Apex Legends API
Use the API at [apexlegendsapi.com](https://apexlegendsapi.com/).

You will need to apply for and prepare an API key in advance.

[apexlegendsapi.com](https://apexlegendsapi.com/)のAPIを使用します。

事前にAPIキーの申請と準備が必要です

### Player stats API
```py
GetApexPlayerStatus(api_key, platform, playerName, *Isuid)
```
Isuid is optional.

If true, playerName will contain uid.

Also, by separating playerName with a comma, multiple player information can be obtained, although the execution time will be longer.

Isuidはオプションです。

Trueの場合playerNameにuidが入ります

また、playerNameをカンマで区切ることによって実行時間は長くなりますが複数プレイヤー情報が取得できます

### Map rotation API
```py
GetApexMapRotation(api_key)
```

### News API
```py
GetApexNews(api_key, *language)
```
language is optional.
By default, en-us is used.

languageはオプションです。
デフォルトではen-usが使用されます

### Server status API
```py
GetApexServerStatus(api_key)
```
As per the [documentation](https://apexlegendsapi.com/documentation.php#buttons-section), you need to display a message on your site when using this API.

[ドキュメント](https://apexlegendsapi.com/documentation.php#buttons-section)にある通り、このAPIを使用する場合にはサイトにメッセージを表示する必要があります。

### Origin / EA API
```py
CallOriginAPI(api_key, PlayerName)
```

## Tracker Network API
Use the API at [Tracker Network APIs for Developers](https://tracker.gg/developers/docs/titles/apex).

You will need to apply for and prepare an API key in advance.

[Tracker Network APIs for Developers](https://tracker.gg/developers/docs/titles/apex)のAPIを使用します。

事前にAPIキーの申請と準備が必要です

### Get an Apex Legends player's profile stats
```py
GetApexPlayerStatus_TRN(api_key, platform, playerName)
```

### Get an Apex Legends player's match history broken up by session
```py
GetApexPlayersMatchHistory_TRN(api_key, platform, playerName)
```