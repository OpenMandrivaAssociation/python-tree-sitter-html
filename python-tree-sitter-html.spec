Name:		python-tree-sitter-html
Version:	0.23.2
Release:	1
Summary:	Tree-sitter html grammar (Python bindings)
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/tree-sitter-html
Source0:	https://files.pythonhosted.org/packages/04/06/ad1c53c79da15bef85939aa022d72301e12a9773e9bb9a5e6a6f65b7753a/tree_sitter_html-0.23.2.tar.gz
# PyPI sdist omits src/tree_sitter/*.h
Source1:	tree-sitter-c-headers.tar.xz
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	clang
Requires:	python%{pyver}dist(tree-sitter)

%description
Tree-sitter grammar for html, compiled from source. Used by
Aider's grep-ast repo-map.

%prep
%autosetup -n tree_sitter_html-0.23.2
tar -C src -xf %{SOURCE1}

%build

%install
export CC=clang
python -m pip install \
	--no-deps --no-build-isolation --no-compile \
	--root %{buildroot} --prefix %{_prefix} \
	.

%files
%doc README.md
%license LICENSE
%{python_sitearch}/tree_sitter_html*
