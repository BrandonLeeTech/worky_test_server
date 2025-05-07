<?php
// 處理請求資料格式
function getRequestData($target, $post) {
    switch ($target) {
        case "post-test":
            return [
                "username" => $post['username'],
            ];

        case "build_employer":
            return [
                "base_url" => $post['base_url'],
                "e_phone" => $post['e_phone'],
                "e_name" => $post['e_name']
            ];

        case "build_labor":
            return [
                "base_url" => $post['base_url'],
                "l_phone" => $post['l_phone'],
                "l_name" => $post['l_name']
            ];

        case "set_account":
            return [
                "base_url" => $post['base_url'],
                "e_phone" => $post['e_phone'],
            ];

        default:
            return ["default" => "data"];
    }
}
