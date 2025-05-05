document.getElementById("formPendaftaran").addEventListener("submit", function (e) {
    e.preventDefault();
  
    const nama = document.getElementById("inputNama").value.trim();
    const email = document.getElementById("inputEmail").value.trim();
    const password = document.getElementById("inputPassword").value;
    const pesan = document.getElementById("pesanValidasi");
  
    if (nama.length <= 3) {
      pesan.textContent = "Nama harus lebih dari 3 karakter.";
      pesan.style.color = "red";
      return;
    }
  
    const regexEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!regexEmail.test(email)) {
      pesan.textContent = "Email tidak valid.";
      pesan.style.color = "red";
      return;
    }
  
    if (password.length < 8) {
      pesan.textContent = "Password minimal 8 karakter.";
      pesan.style.color = "red";
      return;
    }
  
    pesan.textContent = "Pendaftaran berhasil!";
    pesan.style.color = "green";
  });
  