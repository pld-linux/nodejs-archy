Summary:	Renders nested hierarchies with unicode pipes
Name:		nodejs-archy
Version:	0.0.2
Release:	1
License:	MIT/X11
Group:		Libraries
URL:		https://github.com/substack/archy
Source0:	http://registry.npmjs.org/archy/-/archy-%{version}.tgz
# Source0-md5:	382ccc6cdaa38b4eadadcc259faf1931
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Render nested hierarchies with unicode pipes, `npm ls` style.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{nodejs_libdir}/archy
cp -p index.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/archy

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.markdown examples
%{nodejs_libdir}/archy
