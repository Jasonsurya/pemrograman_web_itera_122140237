document.addEventListener('DOMContentLoaded', () => {
    const inputTugas = document.getElementById('inputTugas');
    const tambahBtn = document.getElementById('tambahBtn');
    const daftarTugas = document.getElementById('daftarTugas');

    muatData();

    tambahBtn.addEventListener('click', () => {
        const teks = inputTugas.value.trim();
        if (teks.length > 0) {
            buatItem(teks, false);
            simpanData();
            inputTugas.value = '';
        }
    });

    function buatItem(teks, selesai) {
        const li = document.createElement('li');

        const span = document.createElement('span');
        span.textContent = teks;

        const cek = document.createElement('input');
        cek.type = 'checkbox';
        cek.checked = selesai;
        cek.addEventListener('change', () => {
            li.classList.toggle('completed');
            simpanData();
        });

        const hapus = document.createElement('button');
        hapus.textContent = 'X';
        hapus.addEventListener('click', () => {
            li.remove();
            simpanData();
        });

        li.appendChild(cek);
        li.appendChild(span);
        li.appendChild(hapus);

        if (selesai) li.classList.add('completed');

        daftarTugas.appendChild(li);
    }

    function simpanData() {
        const semuaItem = [];
        daftarTugas.querySelectorAll('li').forEach(li => {
            const span = li.querySelector('span');
            const cek = li.querySelector('input[type="checkbox"]');
            semuaItem.push({
                teks: span.textContent,
                selesai: cek.checked
            });
        });
        localStorage.setItem('daftarTugas', JSON.stringify(semuaItem));
    }

    function muatData() {
        const data = JSON.parse(localStorage.getItem('daftarTugas')) || [];
        data.forEach(item => buatItem(item.teks, item.selesai));
    }
});
