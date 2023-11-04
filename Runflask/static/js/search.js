// search.js
function performSearch() {
    // ดำเนินการค้นหาข้อมูลที่คุณต้องการ
    // ตัวอย่าง: เปิดหน้าเว็บที่ค้นหา
    var searchTerm = document.getElementById("search-input").value;
    var searchUrl = "https://www.google.com/search?query=" + encodeURIComponent(searchTerm);
    window.location.href = searchUrl;
}
// search.js

function checkEnter(event) {
    if (event.key === "Enter") {
        performSearch();
    }
}

function performSearch() {
    // ดำเนินการค้นหาข้อมูลที่คุณต้องการ
    // ตัวอย่าง: เปิดหน้าเว็บที่ค้นหา
    var searchTerm = document.getElementById("search-input").value;
    var searchUrl = "https://www.google.com/search?query=" + encodeURIComponent(searchTerm);
    window.location.href = searchUrl;
}
