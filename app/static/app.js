// Helper function: POST JSON to backend
async function postJSON(url, payload) {
    const res = await fetch(`http://localhost:8000${url}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
    });
    const text = await res.text();
    try {
        return JSON.parse(text);
    } catch {
        return text;
    }
}

// Helper: show result in <pre>
function showResult(id, data) {
    const el = document.getElementById(id);
    el.textContent = typeof data === "string" ? data : JSON.stringify(data, null, 2);
}

// Create PO
async function submitPO(e) {
    e.preventDefault();
    const f = e.target;
    const payload = {
        product_name: f.product_name.value,
        quantity: parseInt(f.quantity.value),
        unit_price: parseFloat(f.unit_price.value),
        supplier: f.supplier.value
    };
    const data = await postJSON("/po/create", payload);
    showResult("result", data);
}

// Track PO
async function submitTrack(e) {
    e.preventDefault();
    const f = e.target;
    const payload = {
        po_id: parseInt(f.po_id.value),
        status_update: f.status_update.value,
        comment: f.comment.value
    };
    const data = await postJSON("/po/track", payload);
    showResult("result", data);
}

// Receipt Confirmation
async function submitReceipt(e) {
    e.preventDefault();
    const f = e.target;
    const payload = {
        po_id: parseInt(f.po_id.value),
        received_quantity: parseInt(f.received_quantity.value),
        received_by: f.received_by.value,
        notes: f.notes.value
    };
    const data = await postJSON("/po/receipt", payload);
    showResult("result", data);
}

// Fetch PO details
async function fetchPODetail(poId, targetId = "result") {
    const res = await fetch(`/po/${poId}`);
    const text = await res.text();
    let data;
    try { data = JSON.parse(text); } catch { data = text; }
    showResult(targetId, data);
}
