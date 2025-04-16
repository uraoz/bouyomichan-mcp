from mcp.server.fastmcp import FastMCP
import requests


mcp = FastMCP("bouyomi-server")

# 棒読みちゃんに読み上げリクエストを送る
def speak_bouyomi(text='ゆっくりしていってね', voice=0, volume=-1, speed=-1, tone=-1):
    res = requests.get(
        'http://localhost:50080/Talk',
        params={
            'text': text,
            'voice': voice,
            'volume': volume,
            'speed': speed,
            'tone': tone
        }
    )
    return res.status_code

@mcp.tool()
async def read_text(text: str, voice: int = 0, volume: int = -1, speed: int = -1, tone: int = -1) -> str:
    """テキストを棒読みちゃんで読み上げます。

    Args:
        text: 読み上げるテキスト
        voice: 音声の種類（0: 女性1、1: 男性1、2: 女性2、...）
        volume: 音量（-1: デフォルト、0-100: 音量レベル）
        speed: 速度（-1: デフォルト、50-200: 速度レベル）
        tone: 音程（-1: デフォルト、50-200: 音程レベル）
    """
    status_code = speak_bouyomi(text, voice, volume, speed, tone)
    
    if status_code == 200:
        return f"「{text}」を音声で読み上げました。(音声: {voice}, 音量: {volume}, 速度: {speed}, 音程: {tone})"
    else:
        return f"読み上げに失敗しました。ステータスコード: {status_code}"

if __name__ == "__main__":
    print("棒読みちゃんMCPサーバーを起動しています...")
    print("このサーバーは読み上げ機能をAIモデルに提供します")
    print("棒読みちゃんが起動していることを確認してください（ポート：50080）")
    
    # MCPサーバーを起動（STDIOトランスポートを使用）
    mcp.run(transport='stdio')