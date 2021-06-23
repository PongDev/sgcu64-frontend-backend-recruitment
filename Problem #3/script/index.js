const form = document.getElementById("register-form");
form.addEventListener("submit", (event) => {
  event.preventDefault();
  const formData = new FormData(form);
  const data = {};
  let success = true;
  for (const [key, value] of formData.entries()) {
    /* USER CODE Begin: Validate data */
    data[key] = value;
    if (success && (data[key].length === 0 || data[key].trim().length === 0)) {
      success = false;
      alert(`กรุณากรอกข้อมูลให้ครบถ้วน`);
    }
    /* USER CODE Begin: Validate data */
  }
  console.log(data);
  const emailRegEX =
    /(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])/;
  if (success && !emailRegEX.test(data["email"])) {
    success = false;
    alert(`รูปแบบ Email ไม่ถูกต้อง`);
  } else if (success && data["password"] !== data["confirmpassword"]) {
    success = false;
    alert(`กรุณากรอก Password ให้ตรงกัน`);
  }
  /* USER CODE Begin: What happened next after recieve form data (Optional) */
  if (success) {
    alert("ลงทะเบียบสำเร็จ");
  }
  /* USER CODE END: What happened next after recieve form data (Optional) */
});
