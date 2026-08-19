/* ===================== DATA ===================== */
const ROOMS = [
  {
    id: 'deluxe',
    name: 'Deluxe Steppe Room',
    price: 145000,
    sqm: 42,
    view: 'Steppe View',
    bed: 'King Bed',
    img: 'https://images.unsplash.com/photo-1611892440504-42a792e24d32?auto=format&fit=crop&w=1200&q=80'
  },
  {
    id: 'executive',
    name: 'Executive Suite',
    price: 210000,
    sqm: 64,
    view: 'River View',
    bed: 'King Bed',
    img: 'https://images.unsplash.com/photo-1590490360182-c33d57733427?auto=format&fit=crop&w=1200&q=80'
  },
  {
    id: 'panorama',
    name: 'Panorama Suite',
    price: 295000,
    sqm: 88,
    view: 'Panoramic City View',
    bed: 'King Bed + Lounge',
    img: 'https://images.unsplash.com/photo-1584132967334-10e028bd69f7?auto=format&fit=crop&w=1200&q=80'
  },
  {
    id: 'presidential',
    name: 'Presidential Residence',
    price: 520000,
    sqm: 140,
    view: 'Ilek River & Skyline',
    bed: 'King Bed + Private Terrace',
    img: 'https://images.unsplash.com/photo-1571896349842-33c89424de2d?auto=format&fit=crop&w=1200&q=80'
  }
];

const AMENITIES = [
  {
    name: 'Spa & Wellness',
    desc: 'A subterranean sanctuary of thermal pools, treatment suites, and a salt-therapy chamber.',
    icon: '<path d="M12 2c2 3 2 5 0 7-2-2-2-4 0-7Z"/><path d="M5 12c3-1 5 0 7 2s-1 5-3 6c-3-1-5-4-4-8Z"/><path d="M19 12c-3-1-5 0-7 2s1 5 3 6c3-1 5-4 4-8Z"/>'
  },
  {
    name: 'Fine Dining',
    desc: 'Qoyandy Table and three additional venues, from open-flame tasting menus to riverside terrace.',
    icon: '<path d="M6 2v8a2 2 0 0 0 4 0V2"/><path d="M8 10v12"/><path d="M17 2c-2 0-3 2-3 5s1 5 3 5 3-2 3-5-1-5-3-5Z"/><path d="M17 12v10"/>'
  },
  {
    name: 'Executive Lounge',
    desc: 'Private check-in, all-day refreshments, and a curated library overlooking the steppe horizon.',
    icon: '<rect x="3" y="7" width="18" height="12" rx="1.5"/><path d="M7 7V5a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v2"/>'
  },
  {
    name: 'Conference Halls',
    desc: 'Five configurable spaces with daylight and full production support, for up to 400 guests.',
    icon: '<rect x="3" y="4" width="18" height="14" rx="1.5"/><path d="M3 16l5-5 4 4 6-6"/>'
  }
];

document.addEventListener('DOMContentLoaded', () => {

  /* ===================== RENDER ROOMS ===================== */
  const roomsGrid = document.getElementById('roomsGrid');
  roomsGrid.innerHTML = ROOMS.map(r => `
    <div class="room-card group rounded-2xl overflow-hidden border border-gold/10 bg-slate-850/40 fade-up" style="background:#101a30">
      <div class="relative h-64 overflow-hidden">
        <img src="${r.img}" alt="${r.name}" class="room-img w-full h-full object-cover"
             onerror="this.onerror=null;this.style.background='linear-gradient(160deg,#16213a,#0b1220)';this.removeAttribute('src');">
        <span class="absolute top-4 left-4 text-xs tracking-widest2 uppercase bg-ink/70 border border-gold/30 text-gold px-3 py-1 rounded-full">${r.sqm} m²</span>
      </div>
      <div class="p-6">
        <h3 class="font-display text-2xl">${r.name}</h3>
        <p class="mt-2 text-sm text-ivory/55">${r.view} · ${r.bed}</p>
        <div class="mt-5 flex items-end justify-between">
          <div>
            <p class="text-gold text-xl font-medium">₸${r.price.toLocaleString('en-US')}</p>
            <p class="text-xs text-ivory/45">per night</p>
          </div>
          <button onclick="openModal('${r.id}')" class="text-sm border border-gold/40 hover:bg-gold hover:text-ink transition-colors rounded-full px-5 py-2">Select Room</button>
        </div>
      </div>
    </div>
  `).join('');

  /* ===================== RENDER AMENITIES ===================== */
  const amenitiesGrid = document.getElementById('amenitiesGrid');
  amenitiesGrid.innerHTML = AMENITIES.map(a => `
    <div class="amenity fade-up border border-gold/10 rounded-2xl p-8 transition-colors">
      <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#c9a24b" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round">${a.icon}</svg>
      <h3 class="font-display text-xl mt-6">${a.name}</h3>
      <p class="mt-3 text-sm text-ivory/60 leading-relaxed">${a.desc}</p>
    </div>
  `).join('');

  /* ===================== ROOM TIER OPTIONS (modal) ===================== */
  const roomTierOptions = document.getElementById('roomTierOptions');
  function renderTierOptions(selectedId){
    roomTierOptions.innerHTML = ROOMS.map(r => `
      <button type="button" data-room="${r.id}"
        class="tier-btn text-left border rounded-xl px-3 py-3 text-xs transition-colors ${r.id === selectedId ? 'border-gold bg-gold/10' : 'border-gold/15 hover:border-gold/40'}">
        <span class="block font-medium">${r.name}</span>
        <span class="block text-ivory/50 mt-1">₸${r.price.toLocaleString('en-US')}</span>
      </button>
    `).join('');
    roomTierOptions.querySelectorAll('.tier-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        roomTierOptions.querySelectorAll('.tier-btn').forEach(b => b.classList.remove('border-gold','bg-gold/10'));
        btn.classList.add('border-gold','bg-gold/10');
        roomTierOptions.dataset.selected = btn.dataset.room;
      });
    });
    roomTierOptions.dataset.selected = selectedId;
  }

  /* ===================== NAV BEHAVIOR ===================== */
  const nav = document.getElementById('siteNav');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) { nav.classList.add('nav-solid'); nav.classList.remove('nav-blur'); }
    else { nav.classList.remove('nav-solid'); nav.classList.add('nav-blur'); }
  });

  const menuBtn = document.getElementById('menuBtn');
  const mobileMenu = document.getElementById('mobileMenu');
  menuBtn.addEventListener('click', () => mobileMenu.classList.toggle('hidden'));
  mobileMenu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => mobileMenu.classList.add('hidden')));

  /* ===================== SCROLL REVEAL ===================== */
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { threshold: .15 });
  document.querySelectorAll('.fade-up').forEach(el => io.observe(el));

  /* ===================== DATE DEFAULTS & VALIDATION ===================== */
  function todayStr(offset=0){
    const d = new Date(); d.setDate(d.getDate()+offset);
    return d.toISOString().split('T')[0];
  }
  ['checkin','mCheckin'].forEach(id => document.getElementById(id).min = todayStr());
  ['checkout','mCheckout'].forEach(id => document.getElementById(id).min = todayStr(1));
  document.getElementById('checkin').value = todayStr(2);
  document.getElementById('checkout').value = todayStr(5);

  function syncCheckoutMin(inId, outId){
    const inEl = document.getElementById(inId), outEl = document.getElementById(outId);
    inEl.addEventListener('change', () => {
      const min = new Date(inEl.value); min.setDate(min.getDate()+1);
      outEl.min = min.toISOString().split('T')[0];
      if (outEl.value && outEl.value <= inEl.value) outEl.value = outEl.min;
    });
  }
  syncCheckoutMin('checkin','checkout');
  syncCheckoutMin('mCheckin','mCheckout');

  /* ===================== MODAL CONTROL ===================== */
  const modal = document.getElementById('bookingModal');
  const panel = modal.querySelector('.modal-panel');

  window.openModal = function(roomId){
    const selected = roomId || 'executive';
    renderTierOptions(selected);
    const heroCheckin = document.getElementById('checkin').value;
    const heroCheckout = document.getElementById('checkout').value;
    if (heroCheckin) document.getElementById('mCheckin').value = heroCheckin;
    if (heroCheckout) document.getElementById('mCheckout').value = heroCheckout;
    document.getElementById('modalConfirmMsg').classList.add('hidden');
    document.getElementById('modalBookingForm').classList.remove('hidden');

    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
    requestAnimationFrame(() => {
      modal.classList.remove('opacity-0');
      panel.classList.remove('opacity-0','translate-y-6');
    });
  };
  window.closeModal = function(){
    modal.classList.add('opacity-0');
    panel.classList.add('opacity-0','translate-y-6');
    document.body.style.overflow = '';
    setTimeout(() => modal.classList.add('hidden'), 350);
  };
  document.addEventListener('keydown', e => { if (e.key === 'Escape') closeModal(); });

  /* ===================== BOOKING EVENT DISPATCH ===================== */
  /* Emits a clean JSON payload on `hotel:booking-request`, ready to POST to a
     FastAPI / REST backend, e.g.:
     document.addEventListener('hotel:booking-request', e => fetch('/api/bookings', {
       method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(e.detail)
     })); */
  function dispatchBooking(payload){
    const event = new CustomEvent('hotel:booking-request', { detail: payload, bubbles: true });
    document.dispatchEvent(event);
    console.log('hotel:booking-request', payload);
    return event;
  }

  document.getElementById('heroBookingForm').addEventListener('submit', e => {
    e.preventDefault();
    const f = e.target;
    openModal(f.roomType.value);
  });

  document.getElementById('modalBookingForm').addEventListener('submit', e => {
    e.preventDefault();
    const f = e.target;
    const roomId = roomTierOptions.dataset.selected;
    const room = ROOMS.find(r => r.id === roomId);

    const payload = {
      event: 'booking_request',
      hotel: 'luxe-aqtobe',
      room: { id: room.id, name: room.name, pricePerNight: room.price, currency: 'KZT' },
      stay: { checkIn: f.checkin.value, checkOut: f.checkout.value, guests: Number(f.guests.value) },
      guest: { fullName: f.fullName.value, email: f.email.value, phone: f.phone.value, requests: f.requests.value || null },
      source: 'web',
      createdAt: new Date().toISOString()
    };

    dispatchBooking(payload);

    f.classList.add('hidden');
    const msg = document.getElementById('modalConfirmMsg');
    msg.textContent = `Thank you, ${payload.guest.fullName.split(' ')[0]}. Your request for the ${room.name} has been received — our reservations team will confirm by email shortly.`;
    msg.classList.remove('hidden');
    setTimeout(closeModal, 3200);
  });

});
