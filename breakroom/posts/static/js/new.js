document.addEventListener("DOMContentLoaded", function () {
  const specification = document.getElementById("specification");
  const howToUse = document.getElementById("how_to_use");
  const availableTime = document.getElementById("availableTime");
  const error_message = document.getElementById("error_message");

  // placeholder 설정 함수
  function placeholderEdit(element, placeholder) {
    element.addEventListener("focus", () => {
      element.placeholder = "";
    });
    element.addEventListener("blur", () => {
      element.placeholder = placeholder;
    });
  }

  // placeholder 설정
  placeholderEdit(specification, "예시: 콘센트 있음, 빈백 있음");
  placeholderEdit(howToUse, "예시: 법학대학 학생만 사용가능, 학생증 지참");
  placeholderEdit(availableTime, "예시: 오전 9:00부터 오후 5:00시까지");

  document.querySelector(".inputs").addEventListener("submit", function (e) {
    e.preventDefault();
    let error_message = document.getElementById("error_message").value;
    if (error_message) {
      Swal.fire({
        title: "공간등록 실패!",
        icon: "error",
        confirmButtonText: "확인",
      });
    } else {
      Swal.fire({
        title: "공간등록 성공!",
        icon: "success",
        confirmButtonText: "확인",
      }).then((result) => {
        if (result.isConfirmed) {
          e.target.submit(); // Submit the form when the confirm button is clicked
        }
      });
    }
  });
});
