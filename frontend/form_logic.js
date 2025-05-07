// form_logic.js

document.addEventListener("DOMContentLoaded", function () {
    const apiSelect = document.getElementById("api_target");
    const form = document.getElementById("testForm");

    const fieldGroups = {
        "get-test": null,
        "post-test": document.getElementById("fields_post-test"),
        "build_employer": document.getElementById("fields_build_employer"),
        "build_labor": document.getElementById("fields_build_labor"),
        "set_account": document.getElementById("fields_set_account")
    };

    const fieldCommon = document.getElementById("field_common");
    const baseUrl = fieldCommon.querySelector('[name="base_url"]');
    const phone = fieldCommon.querySelector('[name="phone"]');

    const requiredFields = {
        "post-test": ["username"],
        "build_employer": ["base_url", "e_name", "phone"],
        "build_labor": ["base_url", "l_name", "phone"],
        "set_account": ["base_url", "phone"]
    };

    function updateFieldVisibility() {
        const selected = apiSelect.value;

        // 清除所有 required
        form.querySelectorAll("input, select").forEach(el => el.required = false);
        // 顯示/隱藏欄位群組
        for (const [key, el] of Object.entries(fieldGroups)) {
            if (el) {
                el.style.display = (key === selected) ? "block" : "none";
            }
        }

        // 控制共用欄位顯示與清空
        const needsCommon = ["build_employer", "build_labor", "set_account"].includes(selected);
        fieldCommon.style.display = needsCommon ? "block" : "none";
        phone.value = "";
        phone.name = "phone";

        // 設定必要欄位
        if (requiredFields[selected]) {
            requiredFields[selected].forEach(name => {
            if (name === "phone") {
                phone.required = true;
            } else {
                const el = form.querySelector(`[name="${name}"]`);
                if (el) el.required = true;
                }
            });
        }

        // 切換 phone 欄位名稱
        if (selected === "build_employer" || selected === "set_account") {
            phone.name = "e_phone";
        } else if (selected === "build_labor") {
            phone.name = "l_phone";
        }
    }

    apiSelect.addEventListener("change", updateFieldVisibility);
    updateFieldVisibility(); // 初始化
});
