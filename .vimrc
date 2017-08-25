set nocompatible              " be iMproved, required
filetype off                  " required

call plug#begin('~/.vim/plugged')

Plug 'plasticboy/vim-markdown'
Plug 'scrooloose/syntastic'
Plug 'tpope/vim-vinegar'
Plug 'scrooloose/nerdtree'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'ctrlpvim/ctrlp.vim'
Plug 'rking/ag.vim'
Plug 'skwp/greplace.vim'
Plug 'airblade/vim-gitgutter'
Plug 'tpope/vim-commentary'
Plug 'junegunn/vim-easy-align'
Plug 'ntpeters/vim-better-whitespace'
Plug 'ervandew/supertab'
Plug 'acoustichero/goldenrod.vim'
Plug 'easymotion/vim-easymotion'
Plug 'nathanaelkane/vim-indent-guides'
Plug 'hwartig/vim-seeing-is-believing'
Plug 'dikiaap/minimalist'
Plug 'tpope/vim-fugitive'
Plug 'tpope/vim-rails'
Plug 'mattn/emmet-vim'
Plug 'vim-ruby/vim-ruby'
Plug 'pangloss/vim-javascript'
Plug 'tpope/vim-rsi'
Plug 'tpope/vim-surround'
Plug 'tpope/vim-ragtag'
Plug 'majutsushi/tagbar'
"Plug 'jiangmiao/auto-pairs'
Plug 'tpope/vim-rake'
Plug 'tpope/vim-bundler'
Plug 'tpope/vim-dispatch'
Plug 'tpope/vim-rvm'
Plug 'tpope/vim-haml'
Plug 'Valloric/YouCompleteMe'
Plug 'flazz/vim-colorschemes'
Plug 'Lokaltog/powerline'
Plug 'tomtom/tcomment_vim'
Plug 'ervandew/sgmlendtag'
"Plug 'Raimondi/delimitMate'

call plug#end()

filetype plugin indent on

" ########## Basic
syntax enable
set encoding=utf-8


" ######### General
set backspace=indent,eol,start " make backspace a more flexible
set backup " make backup files
set backupdir=~/.vim/tmp/backup " where to put backup files
set directory=~/.vim/tmp/swap " directory to place swap files in
set undodir=~/.vim/tmp/undo " directory to place undo files in
set clipboard=unnamedplus " share clipboard
set hidden " you can change buffers without saving
set mouse=a " use mouse everywhere
set noerrorbells " don't make noise
set wildmenu " turn on command line completion wild style
set wildmode=full
set ttyfast " I have a fast terminal
set undofile " make undo possible after the file is closed and reopened
set gdefault " global substitutions are default s/a/b/g
set ttimeoutlen=50  " Make Esc work faster


" ########## VIM User Interface
colorscheme Monokai-Bandit
set background=dark
set t_Co=256 " set terminal 256 color
set incsearch " incremental search aka search as you type
set hlsearch " highlight search matches
set ignorecase " ignore case
set smartcase " but when the query starts with upper character be case sensitive
set laststatus=2 " always show the status line
set lazyredraw " do not redraw while running macros
set linespace=0 " don't insert any extra pixel lines between rows
set nolist " show traling listchars
"set listchars=tab:▸\ ,eol:$,trail:¬,extends:❯,precedes:❮,nbsp:~
set nostartofline " don't move the cursor to first non-blank character after some command    s (:25 e.g.)
set novisualbell " don't blink
set relativenumber " turn on line numbers
set nu " turn on line number on selected line
set report=0 " tell us when anything is changed
set ruler " Always show current positions along the bottom
set shortmess=atToOI " shortens messages to avoid 'press a key' prompt
set showcmd " show the command being typed
set showmode " show current mode
set showmatch " show matching brackets
set scrolloff=5 " Keep 10 lines (top/bottom) for scope
set sidescrolloff=10 " Keep 5 lines at the size
set cursorline " visually mark current line
set showbreak=↪ " indicate wrapped line
hi clear ModeMsg " Disable Color StatusLine on Insert Mode and Visual Mode


" ########## Text Formatting/Layout
set wrap " wrap text
"set textwidth=90 " to 79 characters
"set colorcolumn=85 " and warn me if my line gets over 85 characters
set formatoptions=cqt " see :help fo-table
set infercase " case inferred by default
set shiftround " round the indent to shiftwidth (when at 3 spaces, and I hit > go to 4, n    ot 5)
set expandtab " no real tabs please!
set shiftwidth=4 " auto-indent amount when using >> <<
set softtabstop=4 " when hitting tab or backspace, how many spaces should a tab be (see e    xpandtab)
set tabstop=4 " real tabs should be 4, and they will show with set list on
set autoindent
"set smartindent
match ErrorMsg '^\(<\|=\|>\)\{7\}\([^=].\+\)\?$' " Highlight VCS conflict markers"

autocmd Filetype php setlocal shiftwidth=4 tabstop=4


" ########## Mappings
" my leader key is comma
let mapleader = ","

" another way to esc mode
imap jj <Esc>

" I hit F1 too often when reaching for esc
inoremap <F1> <ESC>
nnoremap <F1> <ESC>
vnoremap <F1> <ESC>

" for edit my .vimrc
nmap <Leader>ev :e $MYVIMRC<cr>

" for move & delete buffer
nmap <Leader>n :bn<cr>
nmap <Leader>p :bp<cr>
nmap <Leader>d :bd<cr>

" for move to each split on NerdTree
nmap <C-h> <C-w><C-h>
nmap <C-j> <C-w><C-j>
nmap <C-k> <C-w><C-k>
nmap <C-l> <C-w><C-l>

" for search
nnoremap / /\v
vnoremap / /\v

" keep search matches in the middle of the window.
nnoremap n nzzzv
nnoremap N Nzzzv

" this key combination gets rid of the search highlights
nmap <leader><space> :noh<cr>

" sudo save
cmap w!! w !sudo tee % >/dev/null

" for page up & page down
noremap <c-u> <c-u>zz
noremap <c-d> <c-d>zz

" Ctags
nmap <Leader>g <C-]>

" for clear highlight search
nmap <Leader><space> :nohlsearch<cr>

" toggle Tagbar plugin
nmap <F8> :TagbarToggle<cr>

" toggle NerdTree plugin
nmap <F12> :NERDTreeToggle<cr>
"nmap <Leader>n :NERDTreeFind<cr>

" open vertical split and switch to it
nnoremap <leader>w <C-w>v<C-w>l

xmap ga <Plug>(EasyAlign)
nmap ga <Plug>(EasyAlign)

" strip all trailing whitespace in the current file
nmap <Leader>W :StripWhitespace<cr>

" enable seeing-is-believing mappings only for Ruby
augroup seeingIsBelievingSettings
  autocmd!

  autocmd FileType ruby nmap <buffer> <Enter> <Plug>(seeing-is-believing-mark-and-run)
  autocmd FileType ruby xmap <buffer> <Enter> <Plug>(seeing-is-believing-mark-and-run)

  autocmd FileType ruby nmap <buffer> <F4> <Plug>(seeing-is-believing-mark)
  autocmd FileType ruby xmap <buffer> <F4> <Plug>(seeing-is-believing-mark)
  autocmd FileType ruby imap <buffer> <F4> <Plug>(seeing-is-believing-mark)

  autocmd FileType ruby nmap <buffer> <F5> <Plug>(seeing-is-believing-run)
  autocmd FileType ruby imap <buffer> <F5> <Plug>(seeing-is-believing-run)
augroup END

" disable arrow keys on insert mode and make up & down arrow as super
no <down> ddp
no <left> <Nop>
no <right> <Nop>
no <up> ddkP
ino <down> <Nop>
ino <left> <Nop>
ino <right> <Nop>
ino <up> <Nop>
vno <down> <Nop>
vno <left> <Nop>
vno <right> <Nop>
vno <up> <Nop>


" ########## Plugins Settings
" NerdTree
let NERDTreeHijackNetrw = 0

" Vim-Airline
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#fnamemod = ':t'
let g:airline#extensions#branch#enabled = 1
let g:airline_powerline_fonts = 1
"let g:airline_theme = 'molokai'
let g:airline_theme = 'minimalist'

" Rubycomplete
let g:rubycomplete_rails=1
let g:rubycomplete_classes_in_global=1
let g:rubycomplete_buffer_loading=1
let g:rubycomplete_include_object=1
let g:rubycomplete_include_objectspace=1

" CtrlP
nmap <leader>r :CtrlPMRUFiles<cr>
nmap <leader>b :CtrlPBuffer<cr>
let g:ctrlp_match_window = 'bottom,order:ttb,min:1,max:20,results:20'

" Vim-Snipmate
"let g:snipMateTrigger = '<c-space>'

" Greplace
set grepprg=ag
let g:grep_cmd_opts = '--line-numbers --noheading'


