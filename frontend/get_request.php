<?php
function getRequestData($target, $post) {
    switch ($target) {
        case "post-test":
            return [
                "username" => $post['username'] ?? '未知用戶',
                "test_type" => $post['test_type'] ?? '未知類型'
            ];

        case "build_employer":
            return [
                "base_url" => "https://next-staging-v211x.api.staging.worky.com.tw/",
                "e_phone" => $post['e_phone'] ?? '0912345678',
                "e_name" => $post['e_name'] ?? '小明商店'
            ];

        default:
            return ["default" => "data"];
    }
}
