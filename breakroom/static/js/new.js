document.addEventListener("DOMContentLoaded", function () {
  let specification = document.getElementById("specification");
  let howToUse = document.getElementById("how_to_use");
  let availableTime = document.getElementById("availableTime");

  specification.addEventListener("focus", () => {
    specification.placeholder = "";
  });
  specification.addEventListener("blur", () => {
    specification.placeholder = "예시: 콘센트 있음, 빈백 있음";
  });
  howToUse.addEventListener("focus", () => {
    howToUse.placeholder = "";
  });
  howToUse.addEventListener("blur", () => {
    howToUse.placeholder = "예시: 법학대학 학생만 사용가능, 학생증 지참";
  });
  availableTime.addEventListener("focus", () => {
    availableTime.placeholder = "";
  });
  availableTime.addEventListener("blur", () => {
    availableTime.placeholder = "예시: 오전 9:00부터 오후 5:00시까지";
  });

  document.querySelector(".inputs").addEventListener("submit", function (e) {
    e.preventDefault();
    Swal.fire({
      title: "공간등록 성공!",
      icon: "success",
      confirmButtonText: "확인",
    }).then((willRedirect) => {
      if (willRedirect) {
        window.location.href = "/"; // 메인페이지로
      }
    });
  });
});
