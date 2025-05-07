<?php
// 處理回應結果
function renderResponse($response) {
    $result = json_decode($response, true);

    echo <<<STYLE
    <style>
        .json-output {
            margin-bottom: 20px;
            font-family: monospace;
            background-color: #f8f8f8;
            padding: 16px;
            border-radius: 8px;
            border: 1px solid #ddd;
            white-space: pre-wrap;
            word-wrap: break-word;
            color: #333;
            font-size: 14px;
        }
        .highlight {
            font-weight: bold;
            color: #007acc;
        }
        .back-btn {
            margin-top: 5px;
            display: inline-block;
            padding: 10px 20px;
            font-size: 14px;
            background: #007acc;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            text-decoration: none;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
    </style>
    STYLE;

    echo "<h3>Response：</h3>";

    echo "<div class='json-output'>";
    foreach (['status', 'result', 'message', 'msg', 'info'] as $field) {
        if (isset($result[$field])) {
            echo "<div><span class='highlight'>{$field}</span>：{$result[$field]}</div>";
        }
    }
    echo "</div>";

    // echo "<pre class='json-output'>" . json_encode($result, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE) . "</pre>";
    echo "<a href='index.html' class='back-btn'>返回首頁</a>";
}
?>
