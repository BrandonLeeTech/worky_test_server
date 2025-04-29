<?php
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

        default:
            return ["default" => "data"];
    }
}
