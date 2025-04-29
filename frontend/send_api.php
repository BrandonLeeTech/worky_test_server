<?php
require_once 'get_request.php';

$api_target = $_POST['api_target'] ?? '';

$environments = [
  "local" => "http://192.168.1.111:8000/",
  "internal" => "https://next-staging-v211x.api.staging.worky.com.tw/",
];
$api_base = $environments["local"];
$api_url = $api_base . $api_target;

$ch = curl_init($api_url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

// 判斷 GET / POST
if (in_array($api_target, ['get-test'])) {
    // 只 GET，不送資料
    curl_setopt($ch, CURLOPT_HTTPGET, true);
} else {
    $data = getRequestData($api_target, $_POST);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'Content-Type: application/json'
    ]);
}

$response = curl_exec($ch);
curl_close($ch);

// 輸出
$result = json_decode($response, true);
echo "<pre>FastAPI Response 原始內容：</pre>";
echo "<pre>" . json_encode($result, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE) . "</pre>";

// 顯示結果欄位
foreach (['status', 'result', 'message', 'msg', 'info'] as $field) {
    if (isset($result[$field])) {
        echo "<p><b>$field</b>：{$result[$field]}</p>";
    }
}

if (curl_errno($ch)) {
    echo "<pre style='color:red;'>cURL 錯誤：" . curl_error($ch) . "</pre>";
}
?>
