// CEC Video Maker Frontend Logic - Sequential Robust Upload & Generator
let selectedFiles = [];
let activeAudio = null;

// DOM Elements
const dropZone = document.getElementById('dropZone');
const clipInput = document.getElementById('clipInput');
const clipList = document.getElementById('clipList');
const clipCountBadge = document.getElementById('clipCountBadge');
const generateBtn = document.getElementById('generateBtn');
const durationSelect = document.getElementById('durationSelect');
const titleInput = document.getElementById('titleInput');
const musicSelect = document.getElementById('musicSelect');
const progressContainer = document.getElementById('progressContainer');
const progressBar = document.getElementById('progressBar');
const progressStep = document.getElementById('progressStep');
const progressPercent = document.getElementById('progressPercent');
const errorContainer = document.getElementById('errorContainer');
const errorMessage = document.getElementById('errorMessage');
const resultCard = document.getElementById('resultCard');
const resultVideo = document.getElementById('resultVideo');
const downloadBtn = document.getElementById('downloadBtn');
const shareBtn = document.getElementById('shareBtn');
const resultMusicName = document.getElementById('resultMusicName');

// Music Modal Elements
const openMusicModalBtn = document.getElementById('openMusicModalBtn');
const closeMusicModalBtn = document.getElementById('closeMusicModalBtn');
const musicModal = document.getElementById('musicModal');
const modalSongList = document.getElementById('modalSongList');
const newSongInput = document.getElementById('newSongInput');
const uploadSongBtn = document.getElementById('uploadSongBtn');

// File Upload Trigger
dropZone.addEventListener('click', () => clipInput.click());

dropZone.addEventListener('dragover', (e) => {
  e.preventDefault();
  dropZone.classList.add('border-brand-500', 'bg-slate-950/80');
});

dropZone.addEventListener('dragleave', () => {
  dropZone.classList.remove('border-brand-500', 'bg-slate-950/80');
});

dropZone.addEventListener('drop', (e) => {
  e.preventDefault();
  dropZone.classList.remove('border-brand-500', 'bg-slate-950/80');
  if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
    addFiles(Array.from(e.dataTransfer.files));
  }
});

clipInput.addEventListener('change', () => {
  if (clipInput.files && clipInput.files.length > 0) {
    addFiles(Array.from(clipInput.files));
    clipInput.value = '';
  }
});

function addFiles(files) {
  const videoFiles = files.filter(f => f.type.startsWith('video/') || f.name.match(/\.(mp4|mov|avi|mkv|webm)$/i));
  if (videoFiles.length === 0) {
    showError('Please select valid video files (.mp4, .mov, etc.)');
    return;
  }
  selectedFiles = selectedFiles.concat(videoFiles);
  renderFileList();
}

function removeFile(index) {
  selectedFiles.splice(index, 1);
  renderFileList();
}

function moveFile(index, direction) {
  const targetIndex = index + direction;
  if (targetIndex < 0 || targetIndex >= selectedFiles.length) return;
  const temp = selectedFiles[index];
  selectedFiles[index] = selectedFiles[targetIndex];
  selectedFiles[targetIndex] = temp;
  renderFileList();
}

function formatFileSize(bytes) {
  if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + ' KB';
  return (bytes / (1024 * 1024)).toFixed(1) + ' MB';
}

function renderFileList() {
  clipList.innerHTML = '';
  clipCountBadge.textContent = `${selectedFiles.length} clip${selectedFiles.length === 1 ? '' : 's'} selected`;

  if (selectedFiles.length > 0) {
    clipCountBadge.className = 'text-xs font-semibold text-brand-400';
  } else {
    clipCountBadge.className = 'text-xs font-medium text-slate-400';
  }

  selectedFiles.forEach((file, idx) => {
    const item = document.createElement('div');
    item.className = 'flex items-center justify-between p-2.5 bg-slate-950 border border-slate-800 rounded-lg text-xs';

    item.innerHTML = `
      <div class="flex items-center space-x-2.5 truncate">
        <span class="w-5 h-5 rounded-full bg-slate-800 text-slate-300 font-bold flex items-center justify-center text-[10px] shrink-0">
          ${idx + 1}
        </span>
        <div class="truncate">
          <p class="font-medium text-slate-200 truncate">${file.name}</p>
          <p class="text-[10px] text-slate-500">${formatFileSize(file.size)}</p>
        </div>
      </div>
      <div class="flex items-center space-x-1 shrink-0 ml-2">
        <button onclick="moveFile(${idx}, -1)" ${idx === 0 ? 'disabled class="opacity-20"' : ''} class="p-1 hover:text-white text-slate-400" title="Move Up">
          <i class="fa-solid fa-arrow-up"></i>
        </button>
        <button onclick="moveFile(${idx}, 1)" ${idx === selectedFiles.length - 1 ? 'disabled class="opacity-20"' : ''} class="p-1 hover:text-white text-slate-400" title="Move Down">
          <i class="fa-solid fa-arrow-down"></i>
        </button>
        <button onclick="removeFile(${idx})" class="p-1 text-rose-400 hover:text-rose-300 ml-1" title="Remove">
          <i class="fa-solid fa-trash-can"></i>
        </button>
      </div>
    `;
    clipList.appendChild(item);
  });
}

function showError(msg) {
  errorMessage.textContent = msg;
  errorContainer.classList.remove('hidden');
  errorContainer.scrollIntoView({ behavior: 'smooth' });
}

function hideError() {
  errorContainer.classList.add('hidden');
  errorMessage.textContent = '';
}

function updateProgress(percent, stepText) {
  const p = Math.min(100, Math.max(0, Math.round(percent)));
  progressBar.style.width = `${p}%`;
  progressPercent.textContent = `${p}%`;
  progressStep.innerHTML = `<i class="fa-solid fa-circle-notch fa-spin"></i> <span>${stepText}</span>`;
}

// Upload a single clip with real-time XHR progress
function uploadClipAsync(jobId, file, index, totalFiles) {
  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    const formData = new FormData();
    formData.append('clip_index', index);
    formData.append('clip', file);

    const baseProgress = (index / totalFiles) * 50;
    const clipWeight = (1 / totalFiles) * 50;

    xhr.upload.onprogress = (e) => {
      if (e.lengthComputable) {
        const filePct = (e.loaded / e.total);
        const overallPct = baseProgress + (filePct * clipWeight);
        updateProgress(
          overallPct,
          `Uploading clip ${index + 1} of ${totalFiles} (${Math.round(filePct * 100)}%)...`
        );
      }
    };

    xhr.onload = () => {
      if (xhr.status >= 200 && xhr.status < 300) {
        try {
          const res = JSON.parse(xhr.responseText);
          resolve(res);
        } catch (e) {
          resolve({});
        }
      } else {
        let errDetail = `Server error (${xhr.status})`;
        try {
          const res = JSON.parse(xhr.responseText);
          if (res.detail) errDetail = res.detail;
        } catch (e) {
          if (xhr.status === 413) errDetail = 'File too large for upload limit. Try shorter clips.';
        }
        reject(new Error(`Failed uploading clip #${index + 1} (${file.name}): ${errDetail}`));
      }
    };

    xhr.onerror = () => {
      reject(new Error(`Network error while uploading clip #${index + 1} (${file.name}). Check connection.`));
    };

    xhr.open('POST', `/api/jobs/${jobId}/upload_clip`, true);
    xhr.send(formData);
  });
}

// Generate Video Handler
generateBtn.addEventListener('click', async () => {
  if (selectedFiles.length < 2) {
    showError('Please select at least 2 video clips (recommended 6–7 clips).');
    return;
  }

  hideError();
  generateBtn.disabled = true;
  generateBtn.classList.add('opacity-50', 'cursor-not-allowed');
  progressContainer.classList.remove('hidden');
  resultCard.classList.add('hidden');
  updateProgress(2, 'Initializing session...');

  try {
    // 1. Initialize session
    const sessionRes = await fetch('/api/jobs/create', { method: 'POST' });
    if (!sessionRes.ok) {
      throw new Error('Could not initialize video session on server.');
    }
    const { job_id } = await sessionRes.json();

    // 2. Upload clips in parallel batches (concurrency=2) for fast mobile transmission (0% -> 50%)
    const total = selectedFiles.length;
    const concurrency = 2;
    for (let i = 0; i < total; i += concurrency) {
      const batch = [];
      for (let j = i; j < Math.min(i + concurrency, total); j++) {
        batch.push(uploadClipAsync(job_id, selectedFiles[j], j, total));
      }
      await Promise.all(batch);
    }

    updateProgress(50, 'All clips uploaded! Starting FFmpeg video engine...');

    // 3. Trigger video generation
    const startForm = new FormData();
    startForm.append('target_duration', durationSelect.value);
    startForm.append('title_text', titleInput.value);
    startForm.append('music_choice', musicSelect.value);

    const startRes = await fetch(`/api/jobs/${job_id}/start`, {
      method: 'POST',
      body: startForm
    });

    if (!startRes.ok) {
      const err = await startRes.json();
      throw new Error(err.detail || 'Failed to start video rendering.');
    }

    // 4. Poll status during rendering (50% -> 100%)
    pollJobStatus(job_id);

  } catch (err) {
    showError(err.message || 'An unexpected error occurred.');
    resetGenerateButton();
  }
});

function pollJobStatus(jobId) {
  let consecutiveErrors = 0;
  const interval = setInterval(async () => {
    try {
      const res = await fetch(`/api/job/${jobId}`);
      if (!res.ok) {
        consecutiveErrors++;
        if (consecutiveErrors >= 10) {
          clearInterval(interval);
          showError('Connection lost or session expired. Please tap "Generate Video" again.');
          resetGenerateButton();
        }
        return;
      }

      consecutiveErrors = 0;
      const job = await res.json();
      updateProgress(job.progress || 55, job.step || 'Processing video...');

      if (job.status === 'completed') {
        clearInterval(interval);
        updateProgress(100, 'Video created successfully!');

        setTimeout(() => {
          progressContainer.classList.add('hidden');
          resultCard.classList.remove('hidden');
          resultVideo.src = `/api/stream/${job.output_file}`;
          resultVideo.load();
          resultVideo.play().catch(() => {});

          downloadBtn.href = `/api/download/${job.output_file}`;
          downloadBtn.setAttribute('download', job.output_file);

          if (job.music_used) {
            resultMusicName.textContent = `🎵 Music: ${job.music_used}`;
          }

          resetGenerateButton();
          resultCard.scrollIntoView({ behavior: 'smooth' });
        }, 500);

      } else if (job.status === 'failed') {
        clearInterval(interval);
        showError('Video generation failed: ' + (job.error || 'FFmpeg error'));
        resetGenerateButton();
      }
    } catch (e) {
      console.error('Error polling status:', e);
      consecutiveErrors++;
      if (consecutiveErrors >= 10) {
        clearInterval(interval);
        showError('Network error while checking status. Please check your connection.');
        resetGenerateButton();
      }
    }
  }, 1000);
}

function resetGenerateButton() {
  generateBtn.disabled = false;
  generateBtn.classList.remove('opacity-50', 'cursor-not-allowed');
  progressContainer.classList.add('hidden');
}

// Native Share API
shareBtn.addEventListener('click', async () => {
  if (navigator.share) {
    try {
      await navigator.share({
        title: 'CEC RSCOE Daily Session Reel',
        text: 'Check out today’s CEC Learning Session Reel!',
        url: window.location.href
      });
    } catch (err) {}
  } else {
    navigator.clipboard.writeText(window.location.href);
    alert('Link copied to clipboard! Share it in WhatsApp.');
  }
});

// Music Modal Management
openMusicModalBtn.addEventListener('click', () => {
  loadSongs();
  musicModal.classList.remove('hidden');
});

closeMusicModalBtn.addEventListener('click', () => {
  if (activeAudio) {
    activeAudio.pause();
    activeAudio = null;
  }
  musicModal.classList.add('hidden');
});

async function loadSongs() {
  try {
    const res = await fetch('/api/songs');
    const data = await res.json();
    modalSongList.innerHTML = '';

    data.songs.forEach(song => {
      const item = document.createElement('div');
      item.className = 'flex items-center justify-between p-2.5 bg-slate-950 border border-slate-800 rounded-lg text-xs';

      item.innerHTML = `
        <div class="flex items-center space-x-2 truncate">
          <i class="fa-solid fa-music text-brand-400"></i>
          <span class="text-slate-300 font-medium truncate">${song.title}</span>
        </div>
        <button onclick="previewAudio('${song.url}', this)" class="p-1.5 rounded-md bg-slate-800 hover:bg-brand-500 hover:text-slate-950 text-slate-300 transition text-[11px] flex items-center gap-1">
          <i class="fa-solid fa-play"></i>
          <span>Play</span>
        </button>
      `;
      modalSongList.appendChild(item);
    });
  } catch (e) {
    console.error('Error loading songs:', e);
  }
}

window.previewAudio = function(url, btn) {
  if (activeAudio) {
    activeAudio.pause();
    document.querySelectorAll('#modalSongList button i').forEach(icon => {
      icon.className = 'fa-solid fa-play';
    });
    if (activeAudio.src.endsWith(url)) {
      activeAudio = null;
      return;
    }
  }

  activeAudio = new Audio(url);
  activeAudio.play();
  const icon = btn.querySelector('i');
  if (icon) icon.className = 'fa-solid fa-pause';

  activeAudio.onended = () => {
    if (icon) icon.className = 'fa-solid fa-play';
    activeAudio = null;
  };
};

uploadSongBtn.addEventListener('click', async () => {
  if (!newSongInput.files || newSongInput.files.length === 0) {
    showError('Please select an audio file first.');
    return;
  }
  const file = newSongInput.files[0];
  const formData = new FormData();
  formData.append('file', file);

  try {
    uploadSongBtn.disabled = true;
    uploadSongBtn.textContent = 'Uploading...';
    const res = await fetch('/api/songs/upload', {
      method: 'POST',
      body: formData
    });
    if (!res.ok) throw new Error('Upload failed');
    alert('Study track added to library!');
    newSongInput.value = '';
    loadSongs();
  } catch (err) {
    showError('Music upload error: ' + err.message);
  } finally {
    uploadSongBtn.disabled = false;
    uploadSongBtn.textContent = 'Add Song';
  }
});
