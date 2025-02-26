import json

# Your JSON list
data = [
         {
          "kanji": "大きい",
          "reading": "ookii",
          "meaning": "big"
        },
        {
          "kanji": "歩く",
          "reading": "aruku",
          "meaning": "walk"
        },
        {
          "kanji": "走る",
          "reading": "hashiru",
          "meaning": "run"
        },
        {
          "kanji": "近く",
          "reading": "chikaku",
          "meaning": "near/close by"
        },
        {
          "kanji": "会う",
          "reading": "au",
          "meaning": "meet/fit"
        },
        {
          "kanji": "場合",
          "reading": "baai",
          "meaning": "situation"
        },
        {
          "kanji": "車",
          "reading": "kuruma",
          "meaning": "car"
        },
        {
          "kanji": "近い",
          "reading": "chikai",
          "meaning": "close"
        },
        {
          "kanji": "遠い",
          "reading": "tooi",
          "meaning": "far"
        },
        {
          "kanji": "仕事",
          "reading": "shigoto",
          "meaning": "job"
        },
        {
          "kanji": "少し",
          "reading": "sukoshi",
          "meaning": "little"
        },
        {
          "kanji": "上る",
          "reading": "noboru",
          "meaning": "climb"
        },
        {
          "kanji": "出す",
          "reading": "dasu",
          "meaning": "put out"
        },
        {
          "kanji": "広い",
          "reading": "hiroi",
          "meaning": "wide"
        },
        {
          "kanji": "短い",
          "reading": "mijikai",
          "meaning": "short(in length)"
        },
        {
          "kanji": "全部",
          "reading": "zenbu",
          "meaning": "all"
        },
        {
          "kanji": "休む",
          "reading": "yasumu",
          "meaning": "to have a break/take day off"
        },
        {
          "kanji": "国",
          "reading": "kuni",
          "meaning": "country"
        },
        {
          "kanji": "白い",
          "reading": "shiroi",
          "meaning": "white"
        },
        {
          "kanji": "赤い",
          "reading": "akai",
          "meaning": "red"
        },
        {
          "kanji": "部屋",
          "reading": "heya",
          "meaning": "room"
        },
        {
          "kanji": "米",
          "reading": "kome",
          "meaning": "rice"
        },
        {
          "kanji": "人",
          "reading": "hito",
          "meaning": "person"
        },
        {
          "kanji": "未だ",
          "reading": "mada",
          "meaning": "yet"
        },
        {
          "kanji": "行く",
          "reading": "iku",
          "meaning": "go"
        },
        {
          "kanji": "有る",
          "reading": "aru",
          "meaning": "exist/have"
        },
        {
          "kanji": "無い",
          "reading": "nai",
          "meaning": "doesn't exist, dont have/opposite of 有る"
        },
        {
          "kanji": "作る",
          "reading": "tsukuru",
          "meaning": "make"
        },
        {
          "kanji": "使う",
          "reading": "tsukau",
          "meaning": "use"
        },
        {
          "kanji": "消す",
          "reading": "kesu",
          "meaning": "switch off"
        },
        {
          "kanji": "春",
          "reading": "haru",
          "meaning": "spring"
        },
        {
          "kanji": "店",
          "reading": "mise",
          "meaning": "shop/store"
        },
        {
          "kanji": "夏",
          "reading": "natsu",
          "meaning": "summer"
        },
        {
          "kanji": "秋",
          "reading": "aki",
          "meaning": "autumn"
        },
        {
          "kanji": "冬",
          "reading": "fuyu",
          "meaning": "winter"
        },
        {
          "kanji": "体",
          "reading": "karada",
          "meaning": "body"
        },
        {
          "kanji": "暑い",
          "reading": "atsui",
          "meaning": "hot(temperature)"
        },
        {
          "kanji": "熱い",
          "reading": "atsui",
          "meaning": "hot (something you feel)"
        },
        {
          "kanji": "寒い",
          "reading": "samui",
          "meaning": "cold"
        },
        {
          "kanji": "暖かい",
          "reading": "atatakai",
          "meaning": "warm"
        },
        {
          "kanji": "新しい",
          "reading": "atarashii",
          "meaning": "new"
        },
        {
          "kanji": "古い",
          "reading": "furui",
          "meaning": "old"
        },
        {
          "kanji": "悪い",
          "reading": "warui",
          "meaning": "bad"
        },
        {
          "kanji": "良い",
          "reading": "ii",
          "meaning": "good"
        },
        {
          "kanji": "思う",
          "reading": "omou",
          "meaning": "think/think so(opinionated)"
        },
        {
          "kanji": "忘れる",
          "reading": "wasureru",
          "meaning": "forgot"
        },
        {
          "kanji": "考える",
          "reading": "kangaeru",
          "meaning": "think(like thinking in your head)"
        },
        {
          "kanji": "決める",
          "reading": "kimeru",
          "meaning": "to decide"
        },
        {
          "kanji": "決まる",
          "reading": "kimaru",
          "meaning": "decided"
        },
        {
          "kanji": "知る",
          "reading": "shiru",
          "meaning": "know"
        },
        {
          "kanji": "一番",
          "reading": "ichiban",
          "meaning": "best/number one"
        },
        {
          "kanji": "住む",
          "reading": "sumu",
          "meaning": "live/reside"
        },
        {
          "kanji": "名前",
          "reading": "namae",
          "meaning": "name"
        },
        {
          "kanji": "食べ物",
          "reading": "tabemono",
          "meaning": "food"
        },
        {
          "kanji": "飲み物",
          "reading": "nomimono",
          "meaning": "drink(like water/soda item)"
        },
        {
          "kanji": "重い",
          "reading": "omoi",
          "meaning": "heavy"
        },
        {
          "kanji": "軽い",
          "reading": "karui",
          "meaning": "light"
        },
        {
          "kanji": "送る",
          "reading": "okuru",
          "meaning": "send"
        },
        {
          "kanji": "取る",
          "reading": "toru",
          "meaning": "take/get"
        },
        {
          "kanji": "待つ",
          "reading": "matsu",
          "meaning": "wait"
        },
        {
          "kanji": "持つ",
          "reading": "motsu",
          "meaning": "possess/have"
        },
        {
          "kanji": "気持ち",
          "reading": "kimochi",
          "meaning": "feeling"
        },
        {
          "kanji": "生きる",
          "reading": "ikiru",
          "meaning": "live(like live life or to be alive)"
        },
        {
          "kanji": "先生",
          "reading": "sensei",
          "meaning": "teacher"
        },
        {
          "kanji": "大学",
          "reading": "daigaku",
          "meaning": "university"
        },
        {
          "kanji": "学生",
          "reading": "gakusei",
          "meaning": "student"
        },
        {
          "kanji": "大学生",
          "reading": "daigakusei",
          "meaning": "university student"
        },
        {
          "kanji": "学校",
          "reading": "gakkou",
          "meaning": "school"
        },
        {
          "kanji": "高校生",
          "reading": "koukousei",
          "meaning": "highschool student"
        },
        {
          "kanji": "教える",
          "reading": "oshieru",
          "meaning": "tell/teach"
        },
        {
          "kanji": "勉強",
          "reading": "benkyou",
          "meaning": "study"
        },
        {
          "kanji": "強い",
          "reading": "tsuyoi",
          "meaning": "strong"
        },
        {
          "kanji": "弱い",
          "reading": "yowai",
          "meaning": "weak"
        },
        {
          "kanji": "引く",
          "reading": "hiku",
          "meaning": "draw/pull"
        },
        {
          "kanji": "質問",
          "reading": "shitsumon",
          "meaning": "question"
        },
        {
          "kanji": "難しい",
          "reading": "muzukashii",
          "meaning": "difficult"
        },
        {
          "kanji": "数",
          "reading": "kazu",
          "meaning": "number"
        },
        {
          "kanji": "勝つ",
          "reading": "katsu",
          "meaning": "win"
        },
        {
          "kanji": "負ける",
          "reading": "makeru",
          "meaning": "lose"
        },
        {
          "kanji": "本当に",
          "reading": "hontouni",
          "meaning": "really"
        },
        {
          "kanji": "要る",
          "reading": "iru",
          "meaning": "need/require"
        },
        {
          "kanji": "時計",
          "reading": "tokei",
          "meaning": "clock/watch"
        },
        {
          "kanji": "払う",
          "reading": "harau",
          "meaning": "pay"
        },
        {
          "kanji": "切る",
          "reading": "kiru",
          "meaning": "cut"
        },
        {
          "kanji": "変える",
          "reading": "kaeru",
          "meaning": "change"
        },
        {
          "kanji": "乗る",
          "reading": "noru",
          "meaning": "ride"
        },
        {
          "kanji": "着る",
          "reading": "kiru",
          "meaning": "wear"
        },
        {
          "kanji": "立つ",
          "reading": "tatsu",
          "meaning": "stand"
        },
        {
          "kanji": "座る",
          "reading": "suwaru",
          "meaning": "sit"
        },
        {
          "kanji": "次",
          "reading": "tsugi",
          "meaning": "next"
        },
        {
          "kanji": "今年",
          "reading": "kotoshi",
          "meaning": "this year"
        },
        {
          "kanji": "長い",
          "reading": "nagai",
          "meaning": "long"
        },
        {
          "kanji": "動く",
          "reading": "ugoku",
          "meaning": "move"
        },
        {
          "kanji": "働く",
          "reading": "hataraku",
          "meaning": "work"
        },
        {
          "kanji": "早い",
          "reading": "hayai",
          "meaning": "early"
        },
        {
          "kanji": "速い",
          "reading": "hayai",
          "meaning": "fast"
        },
        {
          "kanji": "遅い",
          "reading": "osoi",
          "meaning": "slow"
        },
        {
          "kanji": "始める",
          "reading": "hajimeru",
          "meaning": "begin (transitive)"
        },
        {
          "kanji": "始まる",
          "reading": "hajimaru",
          "meaning": "begin (intransitive)"
        },
        {
          "kanji": "終わる",
          "reading": "owaru",
          "meaning": "end/finish"
        },
        {
          "kanji": "終わり",
          "reading": "owari",
          "meaning": "end/conclusion"
        },
        {
          "kanji": "去年",
          "reading": "kyonen",
          "meaning": "last year"
        },
        {
          "kanji": "年",
          "reading": "toshi",
          "meaning": "year/age"
        },
        {
          "kanji": "読む",
          "reading": "yomu",
          "meaning": "read"
        },
        {
          "kanji": "漢字",
          "reading": "kanji",
          "meaning": "chinese character"
        },
        {
          "kanji": "書く",
          "reading": "kaku",
          "meaning": "write"
        },
        {
          "kanji": "覚える",
          "reading": "oboeru",
          "meaning": "remember/learn"
        },
        {
          "kanji": "紙",
          "reading": "kami",
          "meaning": "paper"
        },
        {
          "kanji": "楽しむ",
          "reading": "tanoshimu",
          "meaning": "enjoy(verb)"
        },
        {
          "kanji": "楽しい",
          "reading": "tanoshii",
          "meaning": "fun (adjective)"
        },
        {
          "kanji": "歌う",
          "reading": "utau",
          "meaning": "sing"
        },
        {
          "kanji": "欲しい",
          "reading": "hoshii",
          "meaning": "want"
        },
        {
          "kanji": "色",
          "reading": "iro",
          "meaning": "color"
        },
        {
          "kanji": "茶色",
          "reading": "chairo",
          "meaning": "brown"
        },
        {
          "kanji": "直ぐ",
          "reading": "sugu",
          "meaning": "soon"
        },
        {
          "kanji": "書き直す",
          "reading": "kakinaosu",
          "meaning": "rewrite"
        },
        {
          "kanji": "直る",
          "reading": "naoru",
          "meaning": "repair"
        },
        {
          "kanji": "線",
          "reading": "sen",
          "meaning": "line"
        },
        {
          "kanji": "曲がる",
          "reading": "magaru",
          "meaning": "turn"
        },
        {
          "kanji": "同じ",
          "reading": "onaji",
          "meaning": "same"
        },
        {
          "kanji": "違う",
          "reading": "chigau",
          "meaning": "to be wrong"
        },
        {
          "kanji": "図書館",
          "reading": "toshokan",
          "meaning": "library"
        },
        {
          "kanji": "泊まる",
          "reading": "tomaru",
          "meaning": "stay overnight"
        },
        {
          "kanji": "遊ぶ",
          "reading": "asobu",
          "meaning": "play"
        },
        {
          "kanji": "服",
          "reading": "fuku",
          "meaning": "clothes"
        },
        {
          "kanji": "父",
          "reading": "chichi",
          "meaning": "one's own father"
        },
        {
          "kanji": "母",
          "reading": "haha",
          "meaning": "one's own mother"
        },
        {
          "kanji": "親",
          "reading": "oya",
          "meaning": "parent"
        },
        {
          "kanji": "息子",
          "reading": "musuko",
          "meaning": "son"
        },
        {
          "kanji": "若い",
          "reading": "wakai",
          "meaning": "young"
        },
        {
          "kanji": "彼女",
          "reading": "kanojo",
          "meaning": "she, one's girlfriend"
        },
        {
          "kanji": "彼",
          "reading": "kare",
          "meaning": "he, one's boyfriend"
        },
        {
          "kanji": "弟",
          "reading": "otouto",
          "meaning": "younger brother"
        },
        {
          "kanji": "結婚",
          "reading": "kekkon",
          "meaning": "marry"
        },
        {
          "kanji": "自転車",
          "reading": "jitensha",
          "meaning": "bicycle"
        },
        {
          "kanji": "娘",
          "reading": "musume",
          "meaning": "daughter"
        },
        {
          "kanji": "今日",
          "reading": "kyou",
          "meaning": "today"
        },
        {
          "kanji": "昨日",
          "reading": "kinou",
          "meaning": "yesterday"
        },
        {
          "kanji": "ご主人",
          "reading": "goshujin",
          "meaning": "your husband"
        },
        {
          "kanji": "自分",
          "reading": "jibun",
          "meaning": "oneself"
        },
        {
          "kanji": "答える",
          "reading": "kotaeru",
          "meaning": "answer/reply"
        },
        {
          "kanji": "別",
          "reading": "betsu",
          "meaning": "another/different"
        },
        {
          "kanji": "病気",
          "reading": "byouki",
          "meaning": "illness"
        },
        {
          "kanji": "死ぬ",
          "reading": "shinu",
          "meaning": "die"
        },
        {
          "kanji": "痛い",
          "reading": "itai",
          "meaning": "painful"
        },
        {
          "kanji": "酒",
          "reading": "sake",
          "meaning": "alcohol"
        },
        {
          "kanji": "一杯",
          "reading": "ippai",
          "meaning": "full"
        },
        {
          "kanji": "飛ぶ",
          "reading": "tobu",
          "meaning": "fly"
        },
        {
          "kanji": "飛行機",
          "reading": "hikouki",
          "meaning": "airplane"
        },
        {
          "kanji": "お願い",
          "reading": "onegai",
          "meaning": "favor"
        },
        {
          "kanji": "続く",
          "reading": "tsuzuku",
          "meaning": "continue"
        },
        {
          "kanji": "日記",
          "reading": "nikki",
          "meaning": "diary"
        },
        {
          "kanji": "上",
          "reading": "ue",
          "meaning": "up"
        },
        {
          "kanji": "後ろ",
          "reading": "ushiro",
          "meaning": "back"
        },
        {
          "kanji": "首",
          "reading": "kubi",
          "meaning": "neck"
        },
        {
          "kanji": "頭",
          "reading": "atama",
          "meaning": "head"
        },
        {
          "kanji": "顔",
          "reading": "kao",
          "meaning": "face"
        },
        {
          "kanji": "二",
          "reading": "ni",
          "meaning": "two"
        },
        {
          "kanji": "感じる",
          "reading": "kanjiru",
          "meaning": "feeling"
        },
        {
          "kanji": "探す",
          "reading": "sagasu",
          "meaning": "to search"
        },
        {
          "kanji": "落ちる",
          "reading": "ochiru",
          "meaning": "to fall"
        },
        {
          "kanji": "お手洗い",
          "reading": "otearai",
          "meaning": "toilet"
        },
        {
          "kanji": "手",
          "reading": "te",
          "meaning": "hand"
        },
        {
          "kanji": "冷たい",
          "reading": "tsumetai",
          "meaning": "cold (things you feel)"
        },
        {
          "kanji": "汚い",
          "reading": "kitanai",
          "meaning": "dirty"
        },
        {
          "kanji": "太い",
          "reading": "futoi",
          "meaning": "fat/thick"
        },
        {
          "kanji": "曇る",
          "reading": "kumoru",
          "meaning": "become cloudy"
        },
        {
          "kanji": "神",
          "reading": "kami",
          "meaning": "God"
        },
        {
          "kanji": "建てる",
          "reading": "tateru",
          "meaning": "build/erect"
        },
        {
          "kanji": "左",
          "reading": "hidari",
          "meaning": "left"
        },
        {
          "kanji": "置く",
          "reading": "oku",
          "meaning": "put/leave (things)"
        },
        {
          "kanji": "辺",
          "reading": "hen",
          "meaning": "vicinity/area"
        },
        {
          "kanji": "黄色い",
          "reading": "kiiroi",
          "meaning": "yellow"
        },
        {
          "kanji": "一緒に",
          "reading": "ishoni",
          "meaning": "together"
        },
        {
          "kanji": "緑",
          "reading": "midori",
          "meaning": "green"
        },
        {
          "kanji": "易しい",
          "reading": "yasashii",
          "meaning": "easy"
        },
        {
          "kanji": "留学生",
          "reading": "ryuugakusei",
          "meaning": "international student"
        },
        {
          "kanji": "戻る",
          "reading": "modoru",
          "meaning": "return/go back"
        },
        {
          "kanji": "そば",
          "reading": "soba",
          "meaning": "side/nearby (person)"
        },
        {
          "kanji": "起きる",
          "reading": "okiru",
          "meaning": "occur (event)/get up (from bed)"
        },
        {
          "kanji": "起こる",
          "reading": "okoru",
          "meaning": "happen"
        },
        {
          "kanji": "起こす",
          "reading": "okosu",
          "meaning": "wake up (someone)"
        },
        {
          "kanji": "寝る",
          "reading": "neru",
          "meaning": "to sleep"
        },
        {
          "kanji": "まずい",
          "reading": "mazui",
          "meaning": "bad tasting, bad"
        },
        {
          "kanji": "載せる",
          "reading": "noseru",
          "meaning": "to place on something"
        },
        {
          "kanji": "上手",
          "reading": "jouzu",
          "meaning": "skilled"
        },
        {
          "kanji": "締める",
          "reading": "shimeru",
          "meaning": "close something in a moving manner (fasten/tighten)"
        },
        {
          "kanji": "甘い",
          "reading": "amai",
          "meaning": "sweet"
        },
        {
          "kanji": "辛い",
          "reading": "karai",
          "meaning": "spicy"
        },
        {
          "kanji": "優しい",
          "reading": "yasashii",
          "meaning": "gentle"
        },
        {
          "kanji": "夫",
          "reading": "otto",
          "meaning": "husband"
        },
        {
          "kanji": "妻",
          "reading": "tsuma",
          "meaning": "wife"
        },
        {
          "kanji": "誰",
          "reading": "dare",
          "meaning": "who"
        },
        {
          "kanji": "愛する",
          "reading": "aisuru",
          "meaning": "love"
        },
        {
          "kanji": "笑う",
          "reading": "warau",
          "meaning": "laugh"
        },
        {
          "kanji": "酸っぱい",
          "reading": "suppai",
          "meaning": "sour"
        },
        {
          "kanji": "言葉",
          "reading": "kotoba",
          "meaning": "word"
        },
        {
          "kanji": "呼ぶ",
          "reading": "yobu",
          "meaning": "call"
        },
        {
          "kanji": "足",
          "reading": "ashi",
          "meaning": "feet"
        },
        {
          "kanji": "曜日",
          "reading": "youbi",
          "meaning": "day of the week"
        },
        {
          "kanji": "胸",
          "reading": "mune",
          "meaning": "chest"
        },
        {
          "kanji": "腰",
          "reading": "koshi",
          "meaning": "lower back"
        },
        {
          "kanji": "背",
          "reading": "se",
          "meaning": "tall (as in height)"
        },
        {
          "kanji": "片仮名",
          "reading": "katakana",
          "meaning": "Katakana"
        },
        {
          "kanji": "平仮名",
          "reading": "hiragana",
          "meaning": "Hiragana"
        },
        {
          "kanji": "悲しい",
          "reading": "kanashii",
          "meaning": "sad"
        },
        {
          "kanji": "美しい",
          "reading": "utsukushii",
          "meaning": "beautiful"
        },
        {
          "kanji": "授業",
          "reading": "jugyou",
          "meaning": "class/lesson"
        },
        {
          "kanji": "手伝う",
          "reading": "tetsudau",
          "meaning": "help/assist"
        },
        {
          "kanji": "狭い",
          "reading": "semai",
          "meaning": "narrow"
        },
        {
          "kanji": "触る",
          "reading": "sawaru",
          "meaning": "touch"
        },
        {
          "kanji": "出来る",
          "reading": "dekiru",
          "meaning": "can do"
        },
        {
          "kanji": "嫌い",
          "reading": "kirai",
          "meaning": "dislike"
        },
        {
          "kanji": "浴びる",
          "reading": "abiru",
          "meaning": "take a shower"
        },
        {
          "kanji": "渇く",
          "reading": "kawaku",
          "meaning": "thirsty"
        },
        {
          "kanji": "細い",
          "reading": "hosoi",
          "meaning": "thin/slender"
        },
        {
          "kanji": "安い",
          "reading": "yasui",
          "meaning": "cheap"
        },
        {
          "kanji": "大好き",
          "reading": "daisuki",
          "meaning": "love"
        },
        {
          "kanji": "好き",
          "reading": "suki",
          "meaning": "like"
        },
        {
          "kanji": "低い",
          "reading": "hikui",
          "meaning": "short (in height)"
        },
        {
          "kanji": "閉まる",
          "reading": "shimaru",
          "meaning": "shut in (thing)"
        },
        {
          "kanji": "私",
          "reading": "watashi",
          "meaning": "I/me"
        },
        {
          "kanji": "友達",
          "reading": "tomodachi",
          "meaning": "friend"
        },
        {
          "kanji": "方",
          "reading": "hou",
          "meaning": "direction"
        },
        {
          "kanji": "方(polite form)",
          "reading": "kata",
          "meaning": "person"
        },
        {
          "kanji": "高い",
          "reading": "takai",
          "meaning": "tall"
        },
        {
          "kanji": "昼",
          "reading": "hiru",
          "meaning": "midday"
        },
        {
          "kanji": "元気",
          "reading": "genki",
          "meaning": "health/energetic"
        },
        {
          "kanji": "開ける",
          "reading": "akeru",
          "meaning": "open"
        },
        {
          "kanji": "三日",
          "reading": "mikka",
          "meaning": "3rd day of the month"
        },
        {
          "kanji": "閉める",
          "reading": "shimeru",
          "meaning": "shut in (if it's a person)"
        },
        {
          "kanji": "子供",
          "reading": "kodomo",
          "meaning": "child"
        },
        {
          "kanji": "五",
          "reading": "go",
          "meaning": "five"
        },
        {
          "kanji": "前",
          "reading": "mae",
          "meaning": "front"
        },
        {
          "kanji": "入れる",
          "reading": "ireru",
          "meaning": "to put in"
        },
        {
          "kanji": "聞く",
          "reading": "kiku",
          "meaning": "hear"
        },
        {
          "kanji": "開く",
          "reading": "hiraku",
          "meaning": "open (like opening a book)"
        },
        {
          "kanji": "時間",
          "reading": "jikan",
          "meaning": "time (hour)"
        },
        {
          "kanji": "分かる",
          "reading": "wakaru",
          "meaning": "understand"
        },
        {
          "kanji": "千",
          "reading": "sen",
          "meaning": "thousand"
        },
        {
          "kanji": "後",
          "reading": "ato",
          "meaning": "later"
        },
        {
          "kanji": "水曜日",
          "reading": "suiyoubi",
          "meaning": "Wednesday"
        },
        {
          "kanji": "八つ",
          "reading": "yattsu",
          "meaning": "eith things"
        },
        {
          "kanji": "目",
          "reading": "me",
          "meaning": "eyes"
        },
        {
          "kanji": "午後",
          "reading": "gogo",
          "meaning": "afternoon"
        },
        {
          "kanji": "月曜日",
          "reading": "getsuyoubi",
          "meaning": "Monday"
        },
        {
          "kanji": "月",
          "reading": "tsuki, gatsu",
          "meaning": "moon/moon"
        },
        {
          "kanji": "見える",
          "reading": "mieru",
          "meaning": "be visible"
        },
        {
          "kanji": "出る",
          "reading": "deru",
          "meaning": "leave"
        },
        {
          "kanji": "天気",
          "reading": "tenki",
          "meaning": "weather"
        },
        {
          "kanji": "午前",
          "reading": "gozen",
          "meaning": "morning/A.M."
        },
        {
          "kanji": "七つ",
          "reading": "nanatsu",
          "meaning": "seven things"
        },
        {
          "kanji": "時",
          "reading": "toki",
          "meaning": "time (specific point in time like 'when' but not 'itsu')"
        },
        {
          "kanji": "本",
          "reading": "hon",
          "meaning": "book"
        },
        {
          "kanji": "朝",
          "reading": "asa",
          "meaning": "morning"
        },
        {
          "kanji": "一日",
          "reading": "tsuitachi",
          "meaning": "1st day of the month"
        },
        {
          "kanji": "二日",
          "reading": "futsuka",
          "meaning": "2nd day of the month"
        },
        {
          "kanji": "六日",
          "reading": "muika",
          "meaning": "6th day of the month"
        },
        {
          "kanji": "日曜日",
          "reading": "nichiyoubi",
          "meaning": "Sunday"
        },
        {
          "kanji": "九",
          "reading": "kyuu",
          "meaning": "nine"
        },
        {
          "kanji": "五日",
          "reading": "itsuka",
          "meaning": "5th day of the month"
        },
        {
          "kanji": "土曜日",
          "reading": "doyoubi",
          "meaning": "Saturday"
        },
        {
          "kanji": "女",
          "reading": "onna",
          "meaning": "woman"
        },
        {
          "kanji": "二つ",
          "reading": "futatsu",
          "meaning": "two things"
        },
        {
          "kanji": "晴れる",
          "reading": "hareru",
          "meaning": "to be sunny"
        },
        {
          "kanji": "日",
          "reading": "nichi",
          "meaning": "day"
        },
        {
          "kanji": "晩",
          "reading": "ban",
          "meaning": "evening"
        },
        {
          "kanji": "円",
          "reading": "en",
          "meaning": "circle/yen depending on the context"
        },
        {
          "kanji": "今晩",
          "reading": "konban",
          "meaning": "tonight"
        },
        {
          "kanji": "火曜日",
          "reading": "kayoubi",
          "meaning": "Tuesday"
        },
        {
          "kanji": "夜",
          "reading": "yoru",
          "meaning": "night"
        },
        {
          "kanji": "食べる",
          "reading": "taberu",
          "meaning": "to eat"
        },
        {
          "kanji": "木曜日",
          "reading": "mokuyoubi",
          "meaning": "Thursday"
        },
        {
          "kanji": "五つ",
          "reading": "itsutsu",
          "meaning": "five things"
        },
        {
          "kanji": "飲む",
          "reading": "nomu",
          "meaning": "drink"
        },
        {
          "kanji": "ご飯",
          "reading": "gohan",
          "meaning": "meal"
        },
        {
          "kanji": "六",
          "reading": "roku",
          "meaning": "six"
        },
        {
          "kanji": "四日",
          "reading": "yokka",
          "meaning": "4th day of the month"
        },
        {
          "kanji": "買う",
          "reading": "kau",
          "meaning": "buy"
        },
        {
          "kanji": "見る",
          "reading": "miru",
          "meaning": "see"
        },
        {
          "kanji": "家",
          "reading": "uchi",
          "meaning": "house/home"
        },
        {
          "kanji": "見せる",
          "reading": "miseru",
          "meaning": "show"
        },
        {
          "kanji": "三つ",
          "reading": "mitsu",
          "meaning": "3 things"
        },
        {
          "kanji": "金曜日",
          "reading": "kinyoubi",
          "meaning": "Friday"
        },
        {
          "kanji": "見つける",
          "reading": "mitsukeru",
          "meaning": "find"
        },
        {
          "kanji": "金",
          "reading": "kin,kane",
          "meaning": "gold, friday,money"
        },
        {
          "kanji": "見つかる",
          "reading": "mitsukaru",
          "meaning": "be found"
        },
      
        {
          "kanji": "言う",
          "reading": "iu",
          "meaning": "tell"
        },
        {
          "kanji": "話す",
          "reading": "hanasu",
          "meaning": "speak"
        },
        {
          "kanji": "九つ",
          "reading": "kokonotsu",
          "meaning": "nine things"
        },
        
        {
          "kanji": "万",
          "reading": "man",
          "meaning": "ten thousand"
        },
        {
          "kanji": "時々",
          "reading": "tokidoki",
          "meaning": "sometimes"
        },
        {
          "kanji": "十日",
          "reading": "tooka",
          "meaning": "10th day of the month"
        },
        {
          "kanji": "十",
          "reading": "juu",
          "meaning": "ten"
        },
        {
          "kanji": "髪の毛",
          "reading": "kaminoke",
          "meaning": "hair"
        },
        {
          "kanji": "肩",
          "reading": "kata",
          "meaning": "shoulder"
        },
        {
          "kanji": "鼻",
          "reading": "hana",
          "meaning": "nose"
        },
        {
          "kanji": "腕",
          "reading": "ude",
          "meaning": "arm"
        },
        {
          "kanji": "掛ける",
          "reading": "kakeru",
          "meaning": "to hang, to put on"
        },
        {
          "kanji": "僕",
          "reading": "boku",
          "meaning": "I (used by males)"
        },
        {
          "kanji": "駄目",
          "reading": "dame",
          "meaning": "no good, useless"
        },
        {
          "kanji": "大丈夫",
          "reading": "daijoubu",
          "meaning": "okay, safe"
        },
        {
          "kanji": "風邪",
          "reading": "kaze",
          "meaning": "cold (illness)"
        },
        {
          "kanji": "奇麗",
          "reading": "kirei",
          "meaning": "pretty, clean"
        },
        {
          "kanji": "嬉しい",
          "reading": "ureshii",
          "meaning": "happy"
        },
        {
          "kanji": "閉じる",
          "reading": "tojiru",
          "meaning": "to close"
        },
        {
          "kanji": "億",
          "reading": "oku",
          "meaning": "hundred million"
        },
        {
          "kanji": "寺",
          "reading": "tera",
          "meaning": "temple"
        },
        {
          "kanji": "火",
          "reading": "hi",
          "meaning": "fire"
        },
        {
          "kanji": "木",
          "reading": "ki",
          "meaning": "tree, wood"
        },
        {
          "kanji": "十分",
          "reading": "juubun",
          "meaning": "enough, sufficient"
        },
        {
          "kanji": "分",
          "reading": "bun",
          "meaning": "amount, part, share"
        },
        {
          "kanji": "分ける",
          "reading": "wakeru",
          "meaning": "to divide into parts"
        },
        {
          "kanji": "分かれる",
          "reading": "wakareru",
          "meaning": "to be divided"
        },
        {
          "kanji": "何か",
          "reading": "nanika",
          "meaning": "something"
        },
        {
          "kanji": "何",
          "reading": "nan",
          "meaning": "what, which"
        },
        {
          "kanji": "先ず",
          "reading": "mazu",
          "meaning": "first"
        },
        {
          "kanji": "先",
          "reading": "saki",
          "meaning": "first/go ahead"
        },
        {
          "kanji": "先月",
          "reading": "sengetsu",
          "meaning": "last month"
        },
        {
          "kanji": "先週",
          "reading": "senshuu",
          "meaning": "last week"
        },
        {
          "kanji": "週",
          "reading": "shuu",
          "meaning": "week"
        },
        {
          "kanji": "百",
          "reading": "hyaku",
          "meaning": "hundred"
        },
        {
          "kanji": "九日",
          "reading": "kokonoka",
          "meaning": "9th day of the month"
        },
        {
          "kanji": "今まで",
          "reading": "imamade",
          "meaning": "until now"
        },
        {
          "kanji": "来月",
          "reading": "raigetsu",
          "meaning": "next month"
        },
        {
          "kanji": "来週",
          "reading": "raishuu",
          "meaning": "next week"
        },
        {
          "kanji": "行う",
          "reading": "okonau",
          "meaning": "carry out"
        },
        {
          "kanji": "行き (common usage)",
          "reading": "iki",
          "meaning": "going (common usage)"
        },
        {
          "kanji": "帰り",
          "reading": "kairi",
          "meaning": "go home"
        },
        {
          "kanji": "大きさ",
          "reading": "ookisa",
          "meaning": "size"
        },
        {
          "kanji": "大分",
          "reading": "daibu",
          "meaning": "very / greatly"
        },
        {
          "kanji": "中",
          "reading": "naka",
          "meaning": "inside"
        },
        {
          "kanji": "少年",
          "reading": "shounen",
          "meaning": "young boy"
        },
        {
          "kanji": "少しも",
          "reading": "sukoshimo",
          "meaning": "at all"
        },
        {
          "kanji": "少々",
          "reading": "shoushou",
          "meaning": "a little"
        },
        {
          "kanji": "多く",
          "reading": "ooku",
          "meaning": "a lot / many"
        },
        {
          "kanji": "上がる",
          "reading": "agaru",
          "meaning": "go up, rise / get nervous"
        },
        {
          "kanji": "年上",
          "reading": "toshiue",
          "meaning": "senior"
        },
        {
          "kanji": "上り電車",
          "reading": "nobori densha",
          "meaning": "train that goes toward the city"
        },
        {
          "kanji": "電車",
          "reading": "densha",
          "meaning": "train"
        },
        {
          "kanji": "多い",
          "reading": "ooi",
          "meaning": "big/many/alot"
        },
        {
          "kanji": "駅",
          "reading": "eki",
          "meaning": "railway station"
        },
        {
          "kanji": "道",
          "reading": "michi",
          "meaning": "road"
        },
        {"kanji": "他","reading": "hoka,ta","meaning": "other/others"},
        {"kanji": "来年","reading": "rainen","meaning": "next year"},
        {"kanji": "下げる","reading": "sageru", "meaning": "turn down (volume)"},
        {"kanji": "下がる","reading": "sagaru","meaning": "come down"},
        {"kanji": "下りる","reading": "oriru", "meaning": "go down (stairs)"},
        { "kanji": "下ろす", "reading": "orosu","meaning": "bring down (boxes)"},
        {"kanji": "年下", "reading": "toshishita","meaning": "junior"},
        {"kanji": "一方","reading": "ippo", "meaning": "one way"},
        {"kanji": "行き (used for places)", "reading": "yuki","meaning": "bound for (used for places)"},
        { "kanji": "空く(referring to people)","reading": "suku","meaning": "not crowded"},
        {"kanji": "空く (literal nothing)","reading": "aku","meaning": "empty (literal nothing)"},
        {"kanji": "下り (out of the city)","reading": "kudari","meaning": "going down (out of the city)"},
        {"kanji": "下りる (stairs)","reading": "oriru","meaning": "go down (stairs)"},
      {"kanji": "下ろす (boxes)","reading": "orosu","meaning": "bring down (boxes)" },
        {"kanji": "止める","reading": "yameru,tomeru","meaning": "stop,/turn off"},
        {"kanji": "帰る","reading": "kairu", "meaning": "return/go back"},
        {"kanji": "家 (personal space)","reading": "ie","meaning": "home (personal space)"},
        {"kanji": "外人","reading": "gaijin","meaning": "foreigner"},
        {"kanji": "外", "reading": "soto", "meaning": "outside"},
        {"kanji": "休日", "reading": "kyuujitsu", "meaning": "day off"},
        {"kanji": "休み", "reading": "yasumi", "meaning": "holiday"},
        {"kanji": "力", "reading": "chikara", "meaning": "power/strength"},
        {"kanji": "協力", "reading": "kyouryoku", "meaning": "cooperate"},
        {"kanji": "人口", "reading": "jinko", "meaning": "population"},
        {"kanji": "出口", "reading": "deguchi", "meaning": "exit"},
        {"kanji": "人々", "reading": "hitobito", "meaning": "people"},
        {"kanji": "入り口", "reading": "iriguchi", "meaning": "entrance"},
        {"kanji": "右手", "reading": "migite", "meaning": "right hand"},
        {"kanji": "左手", "reading": "hidarite", "meaning": "left hand"},
        {"kanji": "下手", "reading": "heta", "meaning": "bad/not skilled"},
        {"kanji": "足りる", "reading": "tariru", "meaning": "be satisfied"},
        {"kanji": "足す", "reading": "tasu", "meaning": "add/supplement"},
        {"kanji": "山", "reading": "yama", "meaning": "mountain"},
        {"kanji": "川", "reading": "kawa", "meaning": "river"},
        {"kanji": "空手", "reading": "karate", "meaning": "karate"},
        {"kanji": "空", "reading": "sora", "meaning": "sky"},
        {"kanji": "海外", "reading": "kaigai", "meaning": "abroad/overseas"},
        {"kanji": "海", "reading": "umi", "meaning": "sea/ocean"},
        {"kanji": "毎日", "reading": "mainichi", "meaning": "every day"},
        {"kanji": "毎年", "reading": "maitoshi", "meaning": "every year"},
        {"kanji": "尚", "reading": "nao", "meaning": "in addition, however"},
        {"kanji": "毎週", "reading": "maishuu", "meaning": "every week"},
        {"kanji": "毎月", "reading": "maitsuki", "meaning": "every month"},
        {"kanji": "石", "reading": "ishi", "meaning": "stone"},
        {"kanji": "田んぼ", "reading": "tanbo", "meaning": "rice field"},
        {"kanji": "花", "reading": "hana", "meaning": "flower"},
        {"kanji": "林", "reading": "hayashi", "meaning": "woods"},
        {"kanji": "森", "reading": "mori", "meaning": "forest"},
        {"kanji": "達する", "reading": "tasuru", "meaning": "reach/attain"},
        {"kanji": "売る", "reading": "uru", "meaning": "sell"},
        {"kanji": "子", "reading": "ko", "meaning": "child/kid"},
        {"kanji": "女の子", "reading": "onnanoko", "meaning": "girl/daughter"},
        {"kanji": "男の子", "reading": "otokonoko", "meaning": "boy/baby boy"},
        {"kanji": "私たち", "reading": "watashitachi", "meaning": "we"},
        {"kanji": "家内", "reading": "kanai", "meaning": "my wife"},
        {"kanji": "空気", "reading": "kuuki", "meaning": "atmosphere"},
        {"kanji": "客", "reading": "kyaku", "meaning": "visitor/customer"},
        {"kanji": "気に入る", "reading": "kiniiru", "meaning": "to like/be pleased with"},
        {"kanji": "人気", "reading": "ninki", "meaning": "popular"},
        {"kanji": "雨", "reading": "ame", "meaning": "rain"},
        {"kanji": "雪", "reading": "yuki", "meaning": "snow"},
        {"kanji": "青い", "reading": "aoi", "meaning": "blue (adjective)"},
        {"kanji": "青", "reading": "ao", "meaning": "blue (noun)"},
        {"kanji": "晴れ", "reading": "hare", "meaning": "good weather"},
        {"kanji": "明らか", "reading": "akiraka", "meaning": "obvious"},
        {"kanji": "明るい", "reading": "akarui", "meaning": "cheerful"},
        {"kanji": "明日", "reading": "ashita", "meaning": "tomorrow"},
        {"kanji": "暗い", "reading": "kurai", "meaning": "dark"},
        {"kanji": "昨年", "reading": "sakunen", "meaning": "last year (formal)"},
        {"kanji": "一昨年", "reading": "ototoshi", "meaning": "the year before last"},
        {"kanji": "一昨日", "reading": "ototoi", "meaning": "the day before yesterday"},
        {"kanji": "東", "reading": "higashi", "meaning": "east"},
        {"kanji": "西", "reading": "nishi", "meaning": "west"},
        {"kanji": "南", "reading": "minami", "meaning": "south"},
        {"kanji": "北", "reading": "kita", "meaning": "north"},
        {"kanji": "方向", "reading": "houkou", "meaning": "direction/course"},
        {"kanji": "向かう", "reading": "mukau", "meaning": "to face/go towards"},
        {"kanji": "向こう", "reading": "mukou", "meaning": "other side"},
        {"kanji": "向く", "reading": "muku", "meaning": "to turn toward"},
        {"kanji": "開く", "reading": "aku", "meaning": "to open"},
        {"kanji": "聞こえる", "reading": "kikoeru", "meaning": "to be heard"},
        {"kanji": "年間", "reading": "nenkan", "meaning": "period of one year / a year / per year"},
        {"kanji": "この間", "reading": "kono aida", "meaning": "recently / the other day"},
        {"kanji": "間", "reading": "aida", "meaning": "interval"},
        {"kanji": "人間", "reading": "ningen", "meaning": "human"},
        {"kanji": "高さ", "reading": "takasa", "meaning": "height (referring to size/dimension meters)"},
        {"kanji": "最大", "reading": "saidai", "meaning": "largest"},
        {"kanji": "初めて", "reading": "hajimete", "meaning": "first time"},
        {"kanji": "最初", "reading": "saisho", "meaning": "first / outset"},
        {"kanji": "初め", "reading": "hajime", "meaning": "beginning"},
        {"kanji": "今後", "reading": "kongo", "meaning": "after this / in the future"},
        {"kanji": "後", "reading": "nochi", "meaning": "afterwards"},
        {"kanji": "最後", "reading": "saigo", "meaning": "final / last"},
        {"kanji": "明後日", "reading": "asatte", "meaning": "day after tomorrow"},
        {"kanji": "牛", "reading": "ushi", "meaning": "cow"},
        {"kanji": "下る", "reading": "kudaru", "meaning": "going down from a place"},
        {"kanji": "半分", "reading": "hanbun", "meaning": "half"},
        {"kanji": "姉", "reading": "ane", "meaning": "older sister"},
        {"kanji": "半年", "reading": "hantoshi", "meaning": "half a year"},
        {"kanji": "半月", "reading": "hantsuki", "meaning": "half a month"},
        {"kanji": "半日", "reading": "hannichi", "meaning": "half a day"},
        {"kanji": "毎朝", "reading": "maiasa", "meaning": "every morning"},
        {"kanji": "今朝", "reading": "kesa", "meaning": "this morning"},
        {"kanji": "昼休み", "reading": "hiruyasumi", "meaning": "lunch break"},
        {"kanji": "昼前", "reading": "hirumae", "meaning": "before noon"},
        {"kanji": "昼間", "reading": "hiruma", "meaning": "daytime"},
        {"kanji": "毎晩", "reading": "maiban", "meaning": "every evening"},
        {"kanji": "今夜", "reading": "konya", "meaning": "tonight (formal)"},
        {"kanji": "昨夜", "reading": "yuube", "meaning": "last night"},
        {"kanji": "夜中", "reading": "yonaka", "meaning": "midnight"},
        {"kanji": "夕方", "reading": "yuugata", "meaning": "evening (formal)"},
        {"kanji": "昼食", "reading": "chuushoku", "meaning": "lunch"},
        {"kanji": "朝食", "reading": "choushoku", "meaning": "breakfast"},
        {"kanji": "夕食", "reading": "yuushoku", "meaning": "supper / dinner"},
        {"kanji": "夕飯", "reading": "yuuhan", "meaning": "evening meal"},
        {"kanji": "見方", "reading": "mikata", "meaning": "way of looking / view"},
        {"kanji": "花見", "reading": "hanami", "meaning": "flower viewing"},
        {"kanji": "言い方", "reading": "iikata", "meaning": "way of speaking"},
        {"kanji": "話", "reading": "hanashi", "meaning": "talk / story"},
        {"kanji": "読み", "reading": "yomi", "meaning": "reading / judgment / foresight"},
        {"kanji": "読み方", "reading": "yomikata", "meaning": "way of reading"},
        {"kanji": "語る", "reading": "kataru", "meaning": "talk about something"},
        {"kanji": "言語", "reading": "gengo", "meaning": "language"},
        {"kanji": "英語", "reading": "eigo", "meaning": "English"},
        {"kanji": "文字", "reading": "moji", "meaning": "some writing (character / letter)"},
        {"kanji": "ローマ字", "reading": "romaji", "meaning": "Roman alphabet"},
        {"kanji": "字", "reading": "ji", "meaning": "letter"},
        {"kanji": "書き方", "reading": "kakikata", "meaning": "how to write / way of writing"},
        {"kanji": "覚める", "reading": "sameru", "meaning": "awake"},
        {"kanji": "覚ます", "reading": "samasu", "meaning": "be awake"},
        {"kanji": "大会", "reading": "taikai", "meaning": "mass meeting / tournament"},
        {"kanji": "会話", "reading": "kaiwa", "meaning": "conversation"},
        {"kanji": "話し合う", "reading": "hanashiau", "meaning": "talk over"},
        {"kanji": "間に合う", "reading": "maniau", "meaning": "be in time / can do without"},
        {"kanji": "会社", "reading": "kaisha", "meaning": "company"},
        {"kanji": "社会", "reading": "shakai", "meaning": "society"},
        {"kanji": "社員", "reading": "shain", "meaning": "employee"},
        {"kanji": "仕方", "reading": "shikata", "meaning": "way / method"},
        {"kanji": "食事", "reading": "shokuji", "meaning": "meal / dinner"},
        {"kanji": "火事", "reading": "kaji", "meaning": "fire"},
        {"kanji": "大事", "reading": "daiji", "meaning": "importance"},
        {"kanji": "事故", "reading": "jiko", "meaning": "accident / incident"},
        {"kanji": "工事", "reading": "kouji", "meaning": "construction"},
        {"kanji": "工場", "reading": "koujou", "meaning": "factory"},
        {"kanji": "電話", "reading": "denwa", "meaning": "telephone / phone call"},
        {"kanji": "電気", "reading": "denki", "meaning": "electricity"},
        {"kanji": "駅員", "reading": "ekiin", "meaning": "station employee"},
        {"kanji": "通り", "reading": "toori", "meaning": "passage / street"},
        {"kanji": "通る", "reading": "tooru", "meaning": "pass / go through"},
        {"kanji": "通う", "reading": "kayou", "meaning": "go to and from / frequent a place"},
        {"kanji": "交通事故", "reading": "koutsuujiko", "meaning": "traffic accident"},
        {"kanji": "水道", "reading": "suidou", "meaning": "water service / channel"},
        {"kanji": "車道", "reading": "shadou", "meaning": "road / roadway (car lane)"},
        {"kanji": "年度", "reading": "nendou", "meaning": "year / school year"},
        {"kanji": "今度", "reading": "kondou", "meaning": "this time"},
        {"kanji": "何度", "reading": "nandou", "meaning": "how many times"},
      
        {"kanji": "年間", "reading": "nenkan", "meaning": "period of one year/ a year/ per year"},
        {"kanji": "この間", "reading": "kono aida", "meaning": "the other day"},
        {"kanji": "間", "reading": "aida", "meaning": "interval"},
        {"kanji": "人間", "reading": "ningen", "meaning": "human"},
        {"kanji": "高さ", "reading": "takasa", "meaning": "height(referring to its size/dimention meters)"},
        {"kanji": "最大", "reading": "saidai", "meaning": "largest"},
        {"kanji": "最初", "reading": "saishou", "meaning": "first/outset"},
        {"kanji": "初め", "reading": "Hajime", "meaning": "beginning"},
        {"kanji": "今後", "reading": "kongo", "meaning": "after this, in the future"},
        {"kanji": "後", "reading": "nochi", "meaning": "afterwards"},
        {"kanji": "最後", "reading": "saigo", "meaning": "final/last"},
        {"kanji": "明後日", "reading": "asatte", "meaning": "day after tomorrow"},
        {"kanji": "牛", "reading": "ushi", "meaning": "cow"},
        {"kanji": "下る", "reading": "kudaru", "meaning": "going down from a place"},
        {"kanji": "半分", "reading": "hanbun", "meaning": "half"},
        {"kanji": "姉", "reading": "ane", "meaning": "older sister"},
        {"kanji": "半年", "reading": "hantoshi", "meaning": "half a year"},
        {"kanji": "半月", "reading": "hantsuki", "meaning": "half a month"},
        {"kanji": "半日", "reading": "hannichi", "meaning": "half a day"},
        {"kanji": "毎朝", "reading": "maiasa", "meaning": "every morning"},
        {"kanji": "今朝", "reading": "kesa", "meaning": "this morning"},
        {"kanji": "昼休み", "reading": "hiruyasumi", "meaning": "lunch break"},
        {"kanji": "昼前", "reading": "hirumae", "meaning": "before noon"},
        {"kanji": "昼間", "reading": "hiruma", "meaning": "daytime"},
        {"kanji": "毎晩", "reading": "maiban", "meaning": "every evening"},
        {"kanji": "今夜", "reading": "konya", "meaning": "tonight(formal)"},
        {"kanji": "昨夜", "reading": "yuube", "meaning": "last night"},
        {"kanji": "夜中", "reading": "yonaka", "meaning": "midnight"},
        {"kanji": "夕方", "reading": "yuugata", "meaning": "evening(formal i think)"},
        {"kanji": "昼食", "reading": "chuushoku", "meaning": "lunch"},
        {"kanji": "朝食", "reading": "choushoku", "meaning": "breakfast"},
        {"kanji": "夕食", "reading": "yuushoku", "meaning": "supper/dinner"},
        {"kanji": "夕飯", "reading": "yuuhan", "meaning": "evening meal"},
        {"kanji": "見方", "reading": "mikata", "meaning": "way of looking/view"},
        {"kanji": "花見", "reading": "hanami", "meaning": "flower viewing"},
        {"kanji": "言い方", "reading": "iikata", "meaning": "way of speaking"},
        {"kanji": "話", "reading": "hanashi", "meaning": "talk/story"},
        {"kanji": "読み", "reading": "yomi", "meaning": "reading/judgement, foresight"},
        {"kanji": "読み方", "reading": "yomikata", "meaning": "way of reading"},
        {"kanji": "語る", "reading": "kataru", "meaning": "talk about something"},
        {"kanji": "言語", "reading": "gengo", "meaning": "language"},
        {"kanji": "英語", "reading": "eigo", "meaning": "English"},
        {"kanji": "文字", "reading": "moji", "meaning": "some writing (character/letter)"},
        {"kanji": "ローマ字", "reading": "romaji", "meaning": "roman alphabet"},
        {"kanji": "字", "reading": "ji", "meaning": "letter"},
        {"kanji": "書き方", "reading": "kakikata", "meaning": "how to write/way of writing"},
        {"kanji": "覚める", "reading": "sameru", "meaning": "awake"},
        {"kanji": "覚ます", "reading": "samasu", "meaning": "be awake"},
        {"kanji": "大会", "reading": "taikai", "meaning": "mass meeting/ tournament"},
        {"kanji": "会話", "reading": "kaiwa", "meaning": "conversation"},
        {"kanji": "話し合う", "reading": "hanashiau", "meaning": "talk over"},
        {"kanji": "合う", "reading": "au", "meaning": "meet/fit"},
        {"kanji": "間に合う", "reading": "maniau", "meaning": "be in time, can do without"},
        {"kanji": "会社", "reading": "kaisha", "meaning": "company"},
        {"kanji": "社会", "reading": "shakai", "meaning": "society"},
        {"kanji": "社員", "reading": "shain", "meaning": "employee"},
        {"kanji": "仕方", "reading": "shikata", "meaning": "way method"},
        {"kanji": "食事", "reading": "shokuji", "meaning": "meal/dinner"},
        {"kanji": "火事", "reading": "kaji", "meaning": "fire"},
        {"kanji": "大事", "reading": "daiji", "meaning": "importance"},
        {"kanji": "事故", "reading": "jiko", "meaning": "accident/incident"},
        {"kanji": "工事", "reading": "kouji", "meaning": "construction"},
        {"kanji": "工場", "reading": "koujou", "meaning": "factory"},
        {"kanji": "電話", "reading": "denwa", "meaning": "telephone/phone call"},
        {"kanji": "電気", "reading": "denki", "meaning": "electricity"},
        {"kanji": "駅員", "reading": "ekiin", "meaning": "station employee"},
        {"kanji": "通り", "reading": "toori", "meaning": "passage,street"},
        {"kanji": "通る", "reading": "tooru", "meaning": "pass, go through"},
        {"kanji": "通う", "reading": "kayou", "meaning": "go to and from/frequent a place"},
        {"kanji": "交通事故", "reading": "koutsuujiko", "meaning": "traffic accident"},
        {"kanji": "水道", "reading": "suidou", "meaning": "water service/channel"},
        {"kanji": "車道", "reading": "shadou", "meaning": "road/roadway(specifically refering to the car lane)"},
        {"kanji": "道路", "reading": "douro", "meaning": "road/street"},
        {"kanji": "土地", "reading": "tochi", "meaning": "land"},
        {"kanji": "地図", "reading": "chizu", "meaning": "map/atlas"},
        {"kanji": "止まる", "reading": "tomaru", "meaning": "come to a stop/cease"},
        {"kanji": "止む", "reading": "yamu", "meaning": "stop(like rain)/abate"},
        {"kanji": "歩道", "reading": "hodou", "meaning": "sidewalk/footpath"},
        {"kanji": "渡す", "reading": "watasu", "meaning": "hand over"},
        {"kanji": "渡る", "reading": "wataru", "meaning": "go across"},
        {"kanji": "年度", "reading": "nendou", "meaning": "year/schoolyear"},
        {"kanji": "今度", "reading": "kondou", "meaning": "this time"},
        {"kanji": "何度", "reading": "nandou", "meaning": "how many times"},
        {"kanji": "最近", "reading": "saikin", "meaning": "recently/recent,late"},
        {"kanji": "遠く", "reading": "tooku", "meaning": "great distance"},
        {"kanji": "社長", "reading": "shachou", "meaning": "president of a company"},
        {"kanji": "会長", "reading": "kaichou", "meaning": "chairperson"},
        {"kanji": "長さ", "reading": "nagasa", "meaning": "length"},
        {"kanji": "長男", "reading": "chounan", "meaning": "eldest son"},
        {"kanji": "長女", "reading": "choujo", "meaning": "eldest daughter"},
        {"kanji": "広がる", "reading": "hirogaru", "meaning": "spread out/expanded"},
        {"kanji": "広さ", "reading": "hirosa", "meaning": "area/extent(like how big)"},
        {"kanji": "全体", "reading": "zentai", "meaning": "total/whole"},
        {"kanji": "全く", "reading": "mattaku", "meaning": "entirely/truly,indeed"},
        {"kanji": "安全", "reading": "anzen", "meaning": "safety/security"},
        {"kanji": "一部", "reading": "ichibu", "meaning": "part"},
        {"kanji": "部分", "reading": "bubun", "meaning": "part"},
        {"kanji": "国内", "reading": "kokunai", "meaning": "domestic/internal"},
        {"kanji": "全国", "reading": "zenkoku", "meaning": "the whole country"},
        {"kanji": "外国", "reading": "gaikoku", "meaning": "foreign country"},
        {"kanji": "国会", "reading": "kokkai", "meaning": "parliament"},
        {"kanji": "帰国", "reading": "kikoku", "meaning": "return to one's country"},
        {"kanji": "外国人", "reading": "gaikokujin", "meaning": "foreigner"},
        {"kanji": "外国語", "reading": "gaikokugo", "meaning": "foreign language"},
        {"kanji": "世界", "reading": "sekai", "meaning": "world"},
        {"kanji": "白", "reading": "shiro", "meaning": "white(noun)"},
        {"kanji": "黒い", "reading": "kuroi", "meaning": "black/dark"},
        {"kanji": "黒", "reading": "kuro", "meaning": "black(noun)"},
        {"kanji": "赤ちゃん", "reading": "akachan", "meaning": "baby"},
        {"kanji": "赤", "reading": "aka", "meaning": "red(noun)"},
        {"kanji": "銀行", "reading": "ginko", "meaning": "bank"},
        {"kanji": "銀", "reading": "gin", "meaning": "silver"},
        {"kanji": "地下鉄", "reading": "chikatetsu", "meaning": "subway"},
        {"kanji": "牛肉", "reading": "gyuuniku", "meaning": "beef"},
        {"kanji": "肉", "reading": "niku", "meaning": "flesh/meat"},
        {"kanji": "魚", "reading": "Sakana", "meaning": "fish"},
        {"kanji": "分野", "reading": "bunya", "meaning": "field/sphere"},
        {"kanji": "野菜", "reading": "yasai", "meaning": "vegetable"}
]

# Remove duplicates based on the "kanji" field
unique_data = []
seen_kanji = set()

for entry in data:
    kanji = entry["kanji"]
    if kanji not in seen_kanji:
        unique_data.append(entry)
        seen_kanji.add(kanji)

# Save the unique data to a JSON file
output_file = "unique_data.json"  # Name of the output file
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(unique_data, f, ensure_ascii=False, indent=2)

print(f"Unique data saved to {output_file}")