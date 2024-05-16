let email_ph = document.getElementById("email");
let nickname_ph = document.getElementById("nickname");

email_ph.addEventListener("focus", () => {
  email_ph.placeholder = "";
});
email_ph.addEventListener("blur", () => {
  email_ph.placeholder = "국민대학교 이메일을 입력해주세요.";
});
nickname_ph.addEventListener("focus", () => {
  nickname_ph.placeholder = "";
});
nickname_ph.addEventListener("blur", () => {
  nickname_ph.placeholder = "게시물 작성자로 보일 이름입니다.";
});

document.querySelector(".inputs").addEventListener("submit", function (e) {
  e.preventDefault(); // 확인 버튼을 누르지 않았는데 submit 되는 것을 막음
  let error_message = document.getElementById("error_message").value;
  console.log("Error message:", error_message);
  Swal.fire({
    title: "회원가입 성공!",
    icon: "success",
    confirmButtonText: "확인",
  }).then((result) => {
    if (result.isConfirmed) {
      e.target.submit(); // 확인 버튼을 누르면 submit 실행
    }
  });
});
